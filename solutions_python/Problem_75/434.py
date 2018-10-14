#!/usr/bin/env python

import sys
import re

T = int(sys.stdin.readline())

for ca in range(T):
    line = sys.stdin.readline().split()
    p = 0
    C = int(line[p])
    p+=1
    Cs = line[p:p+C]
    p+=C
    
    D = int(line[p])
    p+=1
    Ds = line[p:p+D]
    p+=D
    
    N = int(line[p])
    p+=1
    Ns = line[p]
    
    # print Cs, Ds, Ns
    
    cur = ''
    for ch in Ns:
        cur += ch
        
                

        for i in Cs:
            if len(cur) >= 2 and sorted(cur[-2:]) == sorted(i[:2]):
                cur = cur[:-2]
                cur += i[2]
        for i in Ds:
            has = False
            if i[0] == i[1]:
                if re.match('%s.*%s' % i[:2], ''.join(cur)):
                    has = True
            else:
                has = i[0] in cur and i[1] in cur
                
            if has:
                cur = ''
            
    print 'Case #%d: [%s]' % (ca+1, ', '.join(cur))
            