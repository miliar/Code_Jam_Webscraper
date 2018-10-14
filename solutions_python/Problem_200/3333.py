# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 19:32:15 2017

@author: cling
"""

def solve(S):
    L = len(S)
    if L==1:
        return S
        
    i = 0
    last_digit = '1'
    state = 0
    check_point = -1
    while i<L:
        if S[i]>last_digit:
            state = 1
            check_point = i
        if S[i]==last_digit:
            state = 0
        if S[i]<last_digit:
            state = -1
            break
        last_digit = S[i]
        i += 1
    if state >= 0:
        return S
    
    if check_point == -1:
        return '9'*(L-1)            
    S = S[:check_point] + str(ord(S[check_point])-ord('1')) + '9'*(L-check_point-1)
    return S
    
def main():
    with open('B-large.in','r') as f:
        line = f.readline()
#        print line,
        i = 1
        for line in f:
            output = solve(line[:-1])
            print 'Case #%d: %s' % (i,output)
            i += 1

if __name__ == '__main__':
    main()
