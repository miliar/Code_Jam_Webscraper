#!/usr/bin/python
'''
Created on 09/04/2010

@author: fsoberon
'''

import re
import sys

def readline():
    return sys.stdin.readline().rstrip('\r\n')

if __name__ == '__main__':
    line = readline()
    T = int(line)
    
    for t in range(1, T + 1):
        line = readline()
        N, K = [int(n) for n in line.split()]
        
        snappers = [False] * N
        for k in range(K):
            for n in range(N):
                previous = snappers[n]
                snappers[n] = not snappers[n]
                if not previous:
                   break
        
        bulb = 'ON'
        for n in range(N):
           if not snappers[n]:
               bulb = 'OFF'
               break
        
        print 'Case #{0}: {1}'.format(t, bulb)

