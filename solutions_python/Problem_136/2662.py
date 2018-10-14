#!/usr/bin/python
'''
Google Code Jam 2014
Qualification Round
Problem B - Cookie Clicker Alpha
2014-04-12
Tyrus Tenneson
'''

import fileinput
import math
import random # for generating test input
import sys

'''
If the farm pays for itself before you reach goal, it's worth.
'''

def solve(case):
    f_cost, f_rate, goal = case
    time_to_buy = [0]
    time_to_win = [ goal / 2 ]
    i = 1
    rate = 2
    while True:
        time_to_buy.append(time_to_buy[i - 1] +
                           f_cost / rate)
        rate += f_rate
        time_to_win.append(time_to_buy[i] + goal / rate)
        if time_to_win[i] > time_to_win[i - 1]:
            return time_to_win[i - 1]
        i += 1

def main():
    lines = [l for l in fileinput.input()]
    T = int(lines[0])
    cases = map(lambda l: map(float, l.split()), lines[1:])
    cases = cases
    for idx, case in enumerate(cases):
        print "Case #{}: {:.7f}".format(idx + 1, solve(case))

# Generate test input
def gen_input(num_cases=100):
    # maxes = (500, 4, 2000) # small
    maxes = (10000, 100, 100000) # large
    print num_cases
    for i in xrange(num_cases):
        print "{} {} {}".format(*map(lambda i: random.uniform(1, i), maxes))
    
if __name__ == "__main__":
    if sys.argv[1] == "gen":
        gen_input()
    else:
        main()
