#!/usr/bin/env python

import sys

f=open(sys.argv[1])

def read(s=None):
    row = f.next().strip().split()
    def int_or_str(s):
        try:
            return int(s)
        except:
            return s

    if s is None:
        return row
        return map(int_or_str, row)

    if len(s) == 1:
        return {'s':str, 'i':int}[s](row[0])
    return tuple({'s':str, 'i':int}[i](j) for i,j in zip(s,row))

def solve():
    s=read('s')
    if len(s) == 1:
        return 1
    base = len(set(s))
    if base == 1:
        base = 2
    digits = {}
    digits[s[0]] = '1'
    rest = list('023456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    res = []
    for t in s:
        if t not in digits:
            digits[t] = rest.pop(0)
        res.append(digits[t])
    #print "".join(res), base
    return int("".join(res),base)
    
         
def main():
    T=read('i')
    for i in range(1,T+1):
        print "Case #%s: %s"%(i,solve())

if __name__ == "__main__":
    main()
