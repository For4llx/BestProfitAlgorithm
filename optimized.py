import csv
import sys
import time

sys.setrecursionlimit(2000)

start_time = time.time()
csv_dataset1 = 'dataset1_Python+P7.csv'

with open(csv_dataset1) as csv_file:
    csv_stocks = csv.reader(csv_file)
    next(csv_stocks)
    stocks = (list(csv_stocks)[:7])

total_cost = []
total_profit = []
all_stocks_names = []
maximum_cost = 500
names = [stock[0] for stock in stocks]
prices = [float(stock[1]) for stock in stocks]
profits = [float(stock[2]) for stock in stocks]
profits_in_euro = [profits[i]/100 * prices[i] for i in range(len(profits))]
ratio = []

for i in range(len(profits_in_euro)):
    if prices[i] != 0:
        ratio.append(profits_in_euro[i]/prices[i])
    else:
        ratio.append(0)

def get_highest_profit():
    if names == []:
        return

    highest_profit = max(ratio)

    if highest_profit > 0:
        index = ratio.index(highest_profit)
        profit = profits.pop(index)
        cost = prices.pop(index)
        name = names.pop(index)
        profit_in_euro = profits_in_euro.pop(index)
        ratio.pop(index)

        if sum(total_cost) + cost <= maximum_cost:
            total_profit.append(profit_in_euro)
            total_cost.append(cost)
            all_stocks_names.append(name)

        get_highest_profit()

get_highest_profit() #O(n²)

print(f'Stock to buy: {all_stocks_names}')
print(f'Total cost: {sum(total_cost)} €')
print(f'Total profit: {round(sum(total_profit), 2)} €')
print(f'Time to complete: {round((time.time() - start_time) * 1000, 0)} ms')
