import csv
import itertools
import time
start_time = time.time()

total_cost = 0
total_profit = 0
all_stocks_names = []
maximum_cost = 500
csv_dataset1 = 'dataset1_Python+P7.csv'

with open(csv_dataset1) as csv_file:
    csv_stocks = csv.reader(csv_file)
    next(csv_stocks)
    stocks = (list(csv_stocks)[:7])
    stocks = list(itertools.product(stocks, repeat=len(stocks))) #O(n^n)

    for stock in stocks:
        names = [data[0] for data in stock]
        cost = sum([float(data[1]) for data in stock])
        profit = sum([(float(data[2])/100) * float(data[1]) for data in stock])

        if cost <= maximum_cost and len(set(names)) == len(names) and profit > total_profit:
            total_cost = cost
            total_profit = profit
            all_stocks_names = names
            
print(f'Stocks to buy: {all_stocks_names}')
print(f'Total cost: {total_cost} €')
print(f'Total profit: {round(total_profit, 2)} €')
print(f'Time to complete: {round((time.time() - start_time) * 1000, 0)} ms')
