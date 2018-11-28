# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 11:53:21 2014

@author: Johnny
"""
import math

name_inp = 'B-large.in'
name_oup = 'B-large.out'
def main():
    output = open(name_oup, 'w')
    with open(name_inp) as inp:
        t = int(inp.readline()[:-1])
        for i in range(1, 1+t):
            c,f,x = [float(k) for k in inp.readline()[:-1].split(' ')]
            n = int(math.ceil(x/c - 2/f))
            s,p = 0, 2
            for j in range(n-1):
                s += c/p
                p += f
            s+= x/p
            output.write("Case #%d: %.7f\n" % (i, s))
    
    output.close()
    
main()