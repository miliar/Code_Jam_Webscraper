#!/usr/bin/env python

def should_buy_farm(target, speed_curr, speed_incr):
    return (target / speed_curr) > (target / (speed_curr + speed_incr))

def solve(line):
    numbers = [float(number) for number in line.split()]
    farm_cost = numbers[0]
    speed_incr = numbers[1]
    target = numbers[2]

    elapsed = float(0)
    speed_curr = float(2)

    take_when_no_buy = target / speed_curr
    take_when_buy = (farm_cost / speed_curr) + (target / (speed_curr + speed_incr))
    while take_when_no_buy > take_when_buy:
        elapsed    += farm_cost / speed_curr
        speed_curr += speed_incr
        take_when_no_buy = target / speed_curr
        take_when_buy = (farm_cost / speed_curr) + (target / (speed_curr + speed_incr))

    elapsed += take_when_no_buy
    return elapsed

    
import sys
#import pdb

if __name__ == '__main__':
    filename_prefix = sys.argv[1]
    filename_in = filename_prefix + ".in"
    filename_out = filename_prefix + ".out"

    with open(filename_in, 'r') as file_in:
        lines = file_in.readlines()

    testcnt = int(lines[0])
    idx = 1

    with open(filename_out, 'w') as file_out:
        #pdb.set_trace()
        for test in range(testcnt):
            res = solve(lines[idx])
            file_out.write("Case #%d: %.7f\n" % (test + 1, res))
            idx += 1
