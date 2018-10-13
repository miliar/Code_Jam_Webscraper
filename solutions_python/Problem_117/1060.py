#!/usr/bin/env python

from __future__ import print_function
import pprint
import re
from operator import itemgetter
import timeit

# won't work out if,
# 1) the lowest number does not appear at least in a row of len m or n

def stol(string, rows, cols):
    """ convert a string representing a game into an list of list """
    gmat = []
    for row in range(rows):
        getter = itemgetter([ (row + c) for c in range(cols) ])
        gmat.append()

def transpose(listoflists):
    """ transpose a string representing a rows x cols matrix into a 
        matrix cols x rows as string 
    """
    return zip(*listoflists)

def heights(game):
    """ get the set of number from a game """
    return sorted(set([column for row in game for column in row]))

def mow(game):
    """ mow the lawn, remove all {lowest} in rows and cols 
    """
    if len(game) == 0:
        return "YES"

    lowest = min(heights(game))
    cols, rows = len(game[0]), len(game)
    # print('-- Problem size: cols=%s, rows=%s' % (cols, rows))    
    pattern = re.compile('(%s){%s,%s}' % (lowest, cols, cols))
    # print('pattern', '%s{%s,%s}' % (lowest, cols, cols))
    
    # print('---- Mowing')
    # pprint.pprint(game)
    for i, row in enumerate(game):
        line = ''.join(['%s' % s for s in row])
        if pattern.match(line):
            # print('------ Cutting row: %s' % i, row)
            # print('------ Next problem would be: ')
            return mow(game[:i] + game[i + 1:])

    game = transpose(game)

    lowest = min(heights(game))
    cols, rows = len(game[0]), len(game)
    # print('-- Problem size: cols=%s, rows=%s' % (cols, rows))    
    pattern = re.compile('(%s){%s,%s}' % (lowest, cols, cols))
    # print('pattern', '%s{%s,%s}' % (lowest, cols, cols))
    
    for i, row in enumerate(game):
        line = ''.join(['%s' % s for s in row])
        if pattern.match(line):
            # print('------ Cutting row: %s' % i, row)
            # print('------ Next problem would be: ')
            return mow(game[:i] + game[i + 1:])

    return "NO"

def main(filename):
    cases = []
    count = 0
    n, m, next = 0, 0, 1 # rows, colums, next case starts at line _
    with open(filename, 'r') as handle:
        for i, line in enumerate(handle):
            if i == 0:
                continue
            if i == next:
                case = []
                count += 1
                # case = ''
                n, m = map(int, line.strip().split())
                next = next + n + 1
                continue
            # case += '%s\n' % (''.join(line.strip().split()))
            # case += '%s' % (''.join(line.strip().split()))
            case += [ map(int, line.strip().split()) ]
            if i == next - 1:
                # print("Case #%s" % count)
                # cases.append(case)
                # solve here ...
                solvable = mow(case)
                # pprint.pprint(case)
                print("Case #%s: %s" % (count, solvable))

    # for i, case in enumerate(cases, start=1):
    #     print('Case #%s' % i)
    #     pprint.pprint(case)
    #     print(heights(case))


if __name__ == '__main__':
    # main(filename='B-sample.in')
    # main(filename='B-example-1.in')
    # main(filename='B-small-attempt0.in')
    main(filename='B-large.in')
    # print(transpose([(2, 1, 2), (2, 1, 2)]))