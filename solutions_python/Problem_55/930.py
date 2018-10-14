#! /usr/bin/env python
import sys


def calculate_money(R, k, g, N):
    """

    R - number of times the ride runs in a day
    k - number of people the ride can fit
    g - list of groups of people
    N - number of groups
    """
    money = 0
    group_at_front_of_line = 0
    for i in range(R):
        people = 0
        added_groups = 0
        while people <= k:
            if people + g[group_at_front_of_line] > k:
                break
            people += g[group_at_front_of_line]
            group_at_front_of_line += 1
            added_groups += 1
            if group_at_front_of_line >= N:
                group_at_front_of_line = 0
            if added_groups >= N:
                break
        money += people
    return money


def main():
    line = sys.stdin.readline()
    # Number of test cases
    T = int(line.strip())
    for i in range(T):
        line = sys.stdin.readline()
        R, k, N = map(int, line.split())
        line = sys.stdin.readline()
        g = map(int, line.split())
        result = calculate_money(R, k, g, N)
        print 'Case #%d: %d' % (i + 1, result)
    return 0


if __name__ == '__main__':
    sys.exit(main())
    
