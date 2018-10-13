
import heapq
import random
import math

def swap(p, i, K):

    return p
    
def Next(st, K, v):
    p = list(st)
    counter = 0
    for i in range(len(p)-K+1):
        if p[i] == '-':
            counter += 1
            for j in range(i, i+K):
                if p[j] == '+':
                    p[j] = '-'
                else:
                    p[j] = '+'
    for pancake in p[len(p)-K:]:
        if pancake == '-':
            return 'IMPOSSIBLE'
    return counter

#input = open(r'sample.in')
#input = open(r'A-small-attempt0.in.txt')
input = open(r'A-large.in.txt')

T = int(input.readline())

sol = []

for i in xrange(T):
    verbose = False
    st, K = input.readline().strip().split()
    sol += [Next(st, int(K), verbose)]
    if not i%10: print i


tofile = True
if tofile:
    with open(r'./outputA.txt', 'w') as output:
        for i in range(len(sol)):
            output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
    print sol


