import heapq
import random
import math

def Next(N, v):
    d= [int(i) for i in str(N)]
    e = 0
    for i in xrange(len(d)-1):
        if d[i] < d[i+1]:
            e = i+1
        if d[i] > d[i+1]:
            d[e] -= 1
            d[e+1:] = (len(d)-e-1)*[9]
            if d[0] == 0:
                d = d[1:]
            return ''.join(str(di) for di in d)
    return N
        
#input = open(r'sample.in')
#input = open(r'B-small-attempt0.in.txt')
input = open(r'B-large.in.txt')

T = int(input.readline())

sol = []

for i in xrange(T):
    verbose = False
    N = int(input.readline().strip())
    sol += [Next(N, verbose)]
    if not i%10: print i


tofile = True
if tofile:
    with open(r'./outputB.txt', 'w') as output:
        for i in range(len(sol)):
            output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
    print sol


