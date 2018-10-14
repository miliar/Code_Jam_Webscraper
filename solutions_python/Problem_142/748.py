# -*- coding: utf-8 -*-
"""
Created on Sat May 03 18:44:17 2014

@author: eidanch
"""


def get_line():
    return raw_input().strip()

formatIntegerList = lambda s: list(map(int,s.split(' ')))

def standard_input():
    T = int(get_line())
    for i in range(T):
        N = int(get_line())
        words = [get_line() for j in range(N)]
        yield (i+1,(N,words))

def removeDuplicates(word):
    result = []
    for c in word:
        if len(result) == 0 or result[-1] != c:
            result.append(c)
    return ''.join(result)
    
def distance(w1,w2):
    n = len(w1)
    i1,i2 = 0,0
    d = 0
    while i1 < len(w1) and i2 < len(w2):
        if w1[i1] != w2[i2]:
            d += 1
            if w1[i1] == w1[i1 - 1]:
                i1 += 1
            else:
                i2 += 1
        else:
            i1 += 1
            i2 += 1
    return d + len(w1) + len(w2) - i1 - i2

def isFeasible(words):
    cleaned = [removeDuplicates(word) for word in words]
    for i in range(len(cleaned) - 1):
        if cleaned[i] != cleaned[i+1]:
            return False
    return True
    
def handle_case(case):
    N,words = case
    if not isFeasible(words):
        return "Fegla Won"
    if N == 2:
        return str(distance(words[0],words[1]))
    return "Not Implemented"
        
def main():
    for i,case in standard_input():
        print "Case #%d: %s" %(i,handle_case(case))        

if __name__ == '__main__':
    main()
    