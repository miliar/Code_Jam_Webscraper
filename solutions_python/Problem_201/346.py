import heapq
import random
import math

def f(N,K):
    n, k = N, K
    while k > 1:
        if n % 2 or not k%2:
            n, k = n/2, k/2
        else:
            n, k = n/2-1, k/2
    if k != 1:
        print 'wtf mate'
    return n/2, (n-1)/2

def Next(N, K, v):
    return '%s %s' % f(N, K)
        
#input = open(r'sample.in')
#input = open(r'C-small-2-attempt0.in.txt')
input = open(r'C-large.in.txt')

T = int(input.readline())

sol = []

for i in xrange(T):
    verbose = False
    N, K = (int(s) for s in input.readline().strip().split())
    sol += [Next(N, K, verbose)]
    if not i%10: print 'case ', i+1
    #print 'case ', i+1


tofile = True
if tofile:
    with open(r'./outputCL.txt', 'w') as output:
        for i in range(len(sol)):
            output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
    print sol


