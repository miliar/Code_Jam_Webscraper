#/usr/bin/python
# -*- coding: UTF-8 -*-
from functools import reduce

__author__ = 'Régis Décamps'

FILENAME='C-small-attempt0'
cache={}

def fast_is_recycled(n,m):
    try:
        return cache[(n,m)]
    except:
        val=is_recycled(n,m)
        cache[(n,m)]=val
        return val

def is_recycled(n,m):
    n=str(n)
    m=str(m)
    #not an optim
    #if sorted(n) != sorted(m):#characters differ:
    #    return 0
    for i in range(1,len(m)):
        if n==m[i:]+m[:i]:
            return 1
    return 0

def count_recycled(a, b):
    retval=0
    for n in range(a,b):
        data=(is_recycled(n,m) for m in range(n+1,b+1))
        retval+=reduce(lambda x,y:x+y, data)
    return retval

if __name__ == '__main__':
    with open('dataset/' + FILENAME + '.in', 'r') as f:
        nbcases = int(f.readline())
        for i in range(1, nbcases + 1):
            data=f.readline().split()
            n=count_recycled(int(data[0]),int(data[1]))
            print("Case #{i}: {result}".format(i=i, result=n))
            