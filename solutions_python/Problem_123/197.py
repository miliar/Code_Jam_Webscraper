from math import sqrt, pow, log, ceil, log10
from sys import stdin, stderr
import random
import collections

# Useful for reduce
def mul(x,y):
    return x * y

def add(x,y):
    return x + y

def max(x, y):
    if x > y:
        return x
    return y

def min(x, y):
    if x < y:
        return x
    return y

def run(array, where, A, max):

    if max == 0:
        # we know it was bad to try to add
        return 1000

    if where >= N:
        return 0

    if A > array[where]:
        # it eats
        A += array[where]
        where += 1
        return run(array, where, A, 1000)
    else:
        # one difficulty: the best would be to add just less than A or to remove all the things on the right (cost: N-where)
        if (A - 1 > 0):
            r1 = 1 + run(array, where, A+(A-1), max-1)
            r2 = N-where
            return min(r1, r2)
        else:
            return N-where

# Main part
T = int(stdin.readline())
# print T

for i in range(1,T+1):

    A, N = map(int, stdin.readline().split())

#    print A, N

    array = map(int, stdin.readline().split())
    array.sort()

    print "Case #" + str(i) + ":",
    print >> stderr, "Running case #" + str(i)

#    print array

    where = 0

    print run(array, where, A, 1000)



