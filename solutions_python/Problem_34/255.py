#!/usr/bin/env python

import sys, re

def main ():
    line = sys.stdin.readline().split();
    l = int(line[0])
    d = int(line[1])
    n = int(line[2])

    dict = [sys.stdin.readline ().strip() for i in range (d)]
    for i in range(n):
        s = sys.stdin.readline().strip().replace (")", "]").replace ("(", "[") + "$"
        count = 0
        p = re.compile (s)
        for w in  dict:
            if (p.match (w)) : count = count +1 
            
        print "Case #" + str(i+1) + ": " + str(count)

main ()


    
        
