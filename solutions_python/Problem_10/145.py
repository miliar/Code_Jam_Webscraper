#!/usr/bin/env python

import sys

sys.setrecursionlimit(1500)





def main():
    
    f = file("A-large.in", "r")
    of = file("output.out", "w")
    
    num_cases = f.readline()

    for x in range(int(num_cases)):
        a_start = []
        
        line = f.readline()
        P = int(line.split(' ')[0])
        K = int(line.split(' ')[1])
        L = int(line.split(' ')[2])
        line2 = f.readline()
        for i in range(L):
            a_start.append(int(line2.split(' ')[i]))
        
        a_start.sort(reverse=True)
        r = 1
        total = 0
        for k1 in range(K):
            m = k1
            p = 1
            while (m < L):
                total = total + (a_start[m] * (p))
                m = m + K
                p = p + 1
            
        
            #val = a_start.pop()
            
        #for r in range()
        
        
        #print a_start
        #if (P * K) < L:
        #    print "Case #%d: %d" % ((p+1),total)
        
        print "Case #%d: %d" % ((x+1),total)
        of.write("Case #%d: %d\n" % ((x+1),total))