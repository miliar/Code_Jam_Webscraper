# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:22:10 2012

@author: Akshay
"""

from operator import itemgetter

def main():
    init = open('C:\Users\Akshay\Documents\CodeJam\A\init.txt')
    i = 3
    letters = {}
    k = 0
    while( i != 0):
        i -= 1
        k = 0
        s = init.readline()
        ans = init.readline()
        for letter in s:
            letters[letter] = ans[k]
            k += 1
    init.close();
    letters['z'] = 'q'
    letters['q'] = 'z'
    
    inp = open('C:\Users\Akshay\Documents\CodeJam\A\input.in')
    T = int(inp.readline())
    case = 1;
    while (T != 0):
        T -= 1
        line = inp.readline()
        s = ""
        for l in line:
            s += letters[l]
        print 'Case #' + str(case) + ': ' + s,
        case += 1
    
            
        
    
    

if __name__ == '__main__':
    main()