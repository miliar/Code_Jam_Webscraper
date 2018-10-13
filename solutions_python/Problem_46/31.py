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
    N=read('i') 
    A=[read('s') for i in range(N)]
    swaps = 0
    for i in range(N):
        if '1' not in A[i] or A[i].rindex("1") <= i: continue
        for j in range(i,N):
            if '1' not in A[j] or A[j].rindex("1") <= i:
                A[i:j+1]=[A[j]]+A[i:j]
                swaps += j-i
                break

    return swaps
         
def main():
    T=read('i')
    for i in range(1,T+1):
        print "Case #%s: %s"%(i,solve())

if __name__ == "__main__":
    main()
