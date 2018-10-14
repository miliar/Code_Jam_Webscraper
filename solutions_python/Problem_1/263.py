#!/usr/bin/python

import sys


stdin = sys.stdin

def next_int():
    return int( stdin.readline() )

def next_line():
    return stdin.readline()

def run():

    tests = next_int()

    for i in range(tests):
        se = next_int()
        xx = []
        res = 0

        for j in range(se):
            xx.append( next_line() )

        qu = next_int()


        t = dict( (x, True) for x in xx )
        count = se

        for j in range(qu):
            y = next_line()

            if t[y] and count == 1:
                count = se
                t = dict( (x, True) for x in xx )
                res += 1

            if t[y]:
                count -= 1
                t[y] = False

        print 'Case #%d: %d' % ( i+1, res)
                    

run()
