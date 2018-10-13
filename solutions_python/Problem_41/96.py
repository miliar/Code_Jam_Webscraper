#!/usr/bin/env python
from itertools import permutations
import sys

def read(s):
    row = sys.stdin.next().strip().split()
    if len(s) == 1:
        return {'s':str, 'i':int}[s](row[0])
    return tuple({'s':str, 'i':int}[i](j) for i,j in zip(s,row))

def solve():
    n = read('s')
    if n == "".join(sorted(n,reverse=True)):
        n='0'+n
    i = len(n)-2
    while n[i] >= n[i+1]:
        i -= 1
    tmp = n[i]
    r=n[i+1:]
    mv = min( x for x in r if x > n[i])
    r="".join(sorted(r.replace(mv,tmp,1)))

    return n[:i]+mv+r
    
         
def main():
    T=read('i')
    for i in range(1,T+1):
        print "Case #%s: %s"%(i,solve())

if __name__ == "__main__":
    main()
