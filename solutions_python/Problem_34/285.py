#!/usr/bin/python
import sys, re

input = sys.stdin

L, D, N = [int(x) for x in input.readline().split()]
vocab = []
for i in range(D):
    vocab.append(input.readline())

patterns = []
for i in range(N):
    pattern = input.readline().replace('(', '[').replace(')', ']')
    p = re.compile(pattern)
    count = 0
    for v in vocab:
        if p.match(v):
            count +=1
    patterns.append(count)



for i in range(len(patterns)):
    print "Case #" + str(i+1) + ": " + str(patterns[i])
