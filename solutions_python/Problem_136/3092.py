from __future__ import division
from sys import stdout


def solve(cost, value, win_condition):
    cookies = cost
    cookies_per_second = 2
    time = cost / cookies_per_second

    if win_condition < cookies:
        print win_condition / cookies_per_second
        return

    while True:
        no_buy = time + (win_condition - cookies) / cookies_per_second
        buy = time + (win_condition - (cookies - cost)) / (cookies_per_second + value)

        if buy < no_buy:
            cookies_per_second += value
            time += (cost / cookies_per_second)
        else:
            print no_buy
            break

num_cases = int(raw_input())

for case in range(1, num_cases + 1):
    cost, value, win_condition = map(float, raw_input().split(' '))

    stdout.write("Case #%i: " % (case))
    solve(cost, value, win_condition)
