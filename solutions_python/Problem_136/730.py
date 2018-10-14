#! /usr/bin/env python3
# Cookie Clicker Alpha


def calculate_time(cost, farm, target):
    total_time = 0
    rate = 2

    while True:
        buy_farm_time = cost / rate
        total_buy_time = buy_farm_time + target / (rate + farm)
        not_buy_time = target / rate

        if total_buy_time < not_buy_time:
            total_time += buy_farm_time
            rate += farm
        else:
            total_time += not_buy_time
            return total_time


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        cost, farm, target = [float(i) for i in input().split()]
        total_time = calculate_time(cost, farm, target)
        print('Case #{}: {:.7f}'.format(i, total_time))


if __name__ == '__main__':
    main()
