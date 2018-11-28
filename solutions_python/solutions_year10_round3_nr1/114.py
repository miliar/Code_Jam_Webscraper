#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, re
        
def main():
    fName = 'A-large'
    fIn = open("%s.in" % fName, 'r')
    fOut = open("%s.out" % fName, 'w')
    
    for t in xrange(int(fIn.readline().strip())):
    
        l = []

        for n in xrange(int(fIn.readline().strip())):
        
            a, b = map(int, fIn.readline().strip().split())
            l.append((a, b))
        
        r = 0
        
        for i in xrange(len(l)):
            for j in xrange(i + 1, len(l)):
                if cmp(l[i][0], l[j][0]) != cmp(l[i][1], l[j][1]):
                    r += 1

        fOut.write("Case #%s: %s\n" % (t+1, r))
        
if __name__ == '__main__': main()
