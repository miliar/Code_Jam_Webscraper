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

def isv(c):
    return (c=='a' or c=='e' or c == 'i' or c == 'o' or c == 'u')

def iscons(c):
    return (not isv(c))

def count(sub):
    #print "study", sub
    c = 0
    maxc = 0
    isrun = 0
    for i in range(len(sub)):
        if iscons(sub[i]):
            c += 1
        else:
            c = 0
        if c > maxc:
            maxc = c
    return maxc

def ans(s, n):
    rep = []
    for i in range(len(s)+1):
        for j in range(len(s)+1):
            if i >= j:
                continue

            sub = s[i:j]

            nb = count(sub)

            if nb >= n:
                rep.append(sub)

#    print rep
#    rep = list(set(rep))
    return len(rep)

# Main part
T = int(stdin.readline())

for i in range(1,T+1):

    print "Case #" + str(i) + ":",

    s, ns = stdin.readline().split()
    n = int(ns)

    #print s, ns
    print ans(s,n)

