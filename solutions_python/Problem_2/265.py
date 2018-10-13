#!/usr/bin/python

import sys


stdin = sys.stdin

buf = stdin.read().split()
buf_pos = -1

def next():
    global buf_pos
    buf_pos += 1
    return buf[ buf_pos ]

def next_int():
    return int( next() )

def next_time():
    hr, mn = next().split(':')
    return int(hr)*60 + int(mn)

def run():

    tests = next_int()

    for i in range(tests):
        timearound = next_int()

        A = next_int()
        B = next_int()
        inA, inB, outA, outB = [], [], [], []

        for a in range(A):
            outA.append( next_time() )
            inB.append( next_time() + timearound )
        
        for a in range(B):
            outB.append( next_time() )
            inA.append( next_time() + timearound )

        def xxx( I, O ):
            I.sort()
            O.sort()
            res, pos = 0, 0

            for x in O:
                #print x, I[pos]
                if pos != len(I) and I[pos] <= x:
                    res +=1
                    pos +=1
            return res


        res_a = A - xxx( inA, outA )
        res_b = B - xxx( inB, outB )

        print 'Case #%d: %d %d' % ( i+1, res_a, res_b)
                    

run()
