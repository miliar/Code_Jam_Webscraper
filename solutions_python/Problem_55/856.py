#!/usr/bin/env python
import sys

def read_input(filename):
    f = open(filename)
    testcases = int(f.readline())
    for i in xrange(testcases):
        rides, places, n_groups = [int(i) for i in f.readline().strip().split()]
        groups = [int(i) for i in f.readline().strip().split()]
        yield rides, places, groups

def solve(rides, places, groups):
    money = 0
    for ride in xrange(rides):
        occupation = 0
        for i, g in enumerate(groups):
            occupation += g
            if occupation > places:
                money += (occupation - g)
                groups = groups[i:] + groups[:i]
                break
        else:
            money += occupation
    return money
    

def main(infile):
    output = (solve(rides, places, groups) for rides, places, groups in read_input(infile))
    print "\n".join("Case #{0}: {1}".format(i+1, answer) for i, answer in enumerate(output))

if __name__ == '__main__':
    main(sys.argv[1])

