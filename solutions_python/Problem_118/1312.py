from __future__ import absolute_import, division, print_function

from math import sqrt
import sys
import time

def candidate_roots():
    temp = [[] for _ in range(100)]
    temp[1] = [1, 2]
    temp[2] = [11, 22]
    
    yield 1
    yield 2
    yield 3
    yield 11
    yield 22
    
    d = 3
    dt = 10
    tt = 100
    ttt = 300
    while True:
        for i in range(tt+1, ttt, tt+1):
            temp[d].append(i)
            yield i
            dtt = dt
            for dd in range(1, d-1, 2):
                for t in temp[dd]:
                    x = i+t*dtt
                    temp[d].append(x)
                    yield x
                dtt //= 10
        if d & 1: dt *= 10
        d += 1
        tt *= 10
        ttt *= 10

def reverse(x):
    r = 0
    while x > 0:
        r *= 10
        r += x%10
        x //= 10
    return r

fair_and_square = []

def precalc(limit=int(1e14)):
    for x in candidate_roots():
        #if x != reverse(x): continue
        xx = x * x
        if xx > limit: break
        if xx != reverse(xx): continue
        fair_and_square.append(xx)
        #print(x, xx)

def solve_case(low, high):
    c = 0
    for p in fair_and_square:
        if low <= p <= high:
            c += 1
    return c

if __name__ == "__main__":
    #start = time.time()
    precalc()
    #stop = time.time()
    #print(stop - start)
    #print(len(fair_and_square))
    #for p in fair_and_square:
    #    print(p)

    for i in range(1, 1+int(sys.stdin.readline().strip())):
        low, high = (int(x) for x in sys.stdin.readline().strip().split(' '))
        print('Case #', i, ': ', solve_case(low, high), sep='', end='\n')
