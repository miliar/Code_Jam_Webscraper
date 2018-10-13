#!/usr/bin/env python
#-*- coding:utf-8 -*-

import math

def main():
    raw_input() # Dummy line
    
    case = 1

    while True:
        pref = "Case #%d: " % case
        try:
            ran = raw_input()
            ran = map(int, ran.split())
            c = 0
            for n in range(ran[0], ran[1]+1):
                if fairsquare(n):
                    c += 1
            print pref + str(c)
        except Exception as e:
            break
        
        case += 1
        
def fairsquare(n):
    if fair(n):
        n = square(n)
        if fair(n):
            return True
            
    return False
     
def square(n):
    s = math.sqrt(n)
    if int(s) == s:
        return int(s)
    else:
        return 12 # a non fair
     
def fair(n):
    n = str(n)
    for i in xrange(len(n)):
        if n[i] != n[-(i+1)]:
            return False
    
    return True        

if __name__ == '__main__':
    main()


