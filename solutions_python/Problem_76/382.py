#!/usr/bin/python
#coding:utf8

"""
#patricks sum is xor?
def add(a,b):
    return a ^ b 
assert add(12L,5L) == 9
assert add(5, 4) == 1
assert add(7, 9) == 14
assert add(50, 10) == 56
"""
from operator import xor, add
def partition(A):
    if reduce(xor, A):
        return "NO"
    menor = min(A) #O(n)
    A.remove(menor)
    return sum(A)


"""
    for i in range(len(A)):
        print get_part( A[:i]+A[i+1:], [A[i]])  


def get_part( subA, subB):
    print subA, subB
    if reduce(xor, subA) == reduce(xor, subA):
        print max( reduce(add, subA),reduce(add, subA)  )
        return True
    return False
"""
#part(A[:] == A[])
#ou A[:] = A[] ^ A[]




if __name__ == '__main__':
    num = input()
    for i in range(num):
        tmp = input()
        case = map(long,raw_input().split())
        print "Case #%s: %s"% (i+1, partition(case))
