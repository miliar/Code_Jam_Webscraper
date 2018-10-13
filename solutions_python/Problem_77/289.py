import sys, os, io
from math import factorial, e
from operator import mul    # or mul=lambda x,y:x*y
from functools import reduce

nCk = lambda n,k: int(round(
    reduce(mul, (float(n-i)/(i+1) for i in range(k)), 1)
))

filename = 'D-large.in'

def read_tokens(f):
    for line in f:
        for token in line.split():
            yield token

def subfactorial(n):
    return float(round(float(factorial(n))/e))

# pontosan k elem kerul a helyere
def P(n, k):
    return float(nCk(n,k))*float(subfactorial(n-k))/float(factorial(n))
    
def expect(n):
    if n == 2:
        return 2.0
    if n == 1:
        return 2.0
    if n == 0:
        return 0.0
    return (1+sum(map(lambda k: P(n, k)*expect(n-k), range(1, n+1))))/(1.0-P(n, 0))

def main():
    with io.open(filename, 'r') as file:
        tokens = read_tokens(file)
        cases = int(next(tokens))
        for case in range(cases):
            n = int(next(tokens))
            l = []
            for i in range(n):
                l.append(int(next(tokens)))
            errors = len([1 for (a, b) in zip(l, sorted(l)) if a!=b])
            #print(errors)
            print("Case #%d: %f"%(case+1, float(errors)))
            

main()