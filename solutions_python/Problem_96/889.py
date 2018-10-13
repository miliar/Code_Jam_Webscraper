#!/usr/bin/env python
# encoding: utf-8

import sys

T = int(sys.stdin.readline())

for i in range(T):
    result = 0
    line = map(int,sys.stdin.readline().split())
    qtdGooglers = line[0]
    surprise = line[1]
    p = line[2]
    grades = line[3:]
    
    for grade in grades:
        if ((p-1)*3 < grade):
            result+=1
        else:
            if (surprise >= 1):
                count = p + p-2 + p-2
                if (grade >= p and grade >= count):
                    result+=1
                    surprise-=1
                
    print 'Case #%d: %s ' % (i+1, result)
    