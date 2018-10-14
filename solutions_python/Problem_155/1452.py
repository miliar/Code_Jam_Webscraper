#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

def main():
    in_file = open("A-large.in", mode='r')
    out_file = open("A-large.out", mode='w')

    lines = in_file.readlines()      
    T = int(lines[0])
    
    for i in xrange(T):
        line = lines[i + 1]
        SMax, S = line.split()
        SMax = int(SMax)
        S = [int(x) for x in S]
        N = 0
        M = 0
        for j in xrange(SMax+1):
            K = 0 if j<=M else j-M
            M += (S[j]+K)             
            N += K
        ans = N
        
        out_file.write("Case #" + str(i+1) + ": " + str(ans) + "\n") 
        #print("Case #" + str(i+1) + ": " + str(ans) + "\n")
        
        
    in_file.close()
    out_file.close()


if __name__ == '__main__':
    main()
