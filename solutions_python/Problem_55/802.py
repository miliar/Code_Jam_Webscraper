#!/usr/bin/python
'''
Created on 12/04/2010

@author: fsoberon
'''
import sys

def readline():
    return sys.stdin.readline().rstrip('\r\n')

if __name__ == '__main__':
    line = readline()
    T = int(line)
    
    for t in range(1, T + 1):
        line = readline()
        R, k, N = [int(n) for n in line.split()]
        line = readline()
        g = tuple([int(n) for n in line.split()])
        
        money = 0
        
        for r in range(R):
            passengers = 0
            index = 0
            
            while index < N and g[index] + passengers <= k:
                passengers += g[index]
                index += 1
            
            money += passengers
            g = g[index:] + g[:index]
        
        print 'Case #{0}: {1}'.format(t, money)

