#!/usr/bin/python
from collections import deque
from sys import *

if __name__ == '__main__':

    T = stdin.readline().strip('\r\n')
    for t in range(int(T)):
        money = 0
        [R,k,N] = map(int, stdin.readline().rstrip('\r\n').split(' '))
        d = deque(map(int, stdin.readline().rstrip('\r\n').split(' ')))

        for r in range(R):
            i = d[0]
            j = 1
            while 1:
                if (1 < len(d)) and (j < len(d)) and ((i+d[j]) <= k):
                    i += d[j]
                    j += 1
                else: break
            d.rotate(-j)
            money += i
        print "Case #"+ str(t+1) + ": " + str(money)
