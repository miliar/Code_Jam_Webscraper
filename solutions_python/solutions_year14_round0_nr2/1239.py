#!/usr/bin/python

import sys

DEF_RATE = 2

def solve(C, F, X):
    farms = 0
    total_time = 0
    while True:
        # What's better, just wait of buy a farm?
        income = DEF_RATE + farms * F
        just_wait = X / income
        new_income = DEF_RATE + (farms + 1) * F
        buy_farm_and_wait = C / income + X / new_income
        if just_wait < buy_farm_and_wait:
            total_time += just_wait
            return total_time
        else:
            total_time += C / income
            farms += 1


def main(filename):
    with open(filename) as f:
        for case_num in range(int(f.readline())):
            C, F, X = map(float, f.readline().split(' '))
            print 'Case #{}: {:.7f}'.format(case_num + 1, solve(C, F, X))


if __name__ == "__main__":
    main(sys.argv[1])
