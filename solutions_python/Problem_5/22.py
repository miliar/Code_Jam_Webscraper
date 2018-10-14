#!/usr/bin/env python

import sys

readline = lambda : sys.stdin.readline()

C = int(readline())

def next_batch(choices, i=0):
    if i == len(choices):
        return False
    if choices[i] == 0:
        choices[i] = 1
        return True
    else:
        choices[i] = 0
        return next_batch(choices, i+1)

for c in range(C):
    N = int(readline())
    M = int(readline())
    customers = []
    for m in range(M):
        likes = []
        line = map(int, readline().split())
        for i in range(1, len(line), 2):
            likes.append((line[i]-1, line[i+1]))
        customers.append(likes)
    
    batch = [0]*N
    while True:
        works = True
        for cust in customers:
            happy = False
            for a, b in cust:
                if batch[a] == b:
                    happy = True
                    break
            if not happy:
                works = False
                break

        if works or not next_batch(batch):
            break
    
    if works:
        print 'Case #%d: %s' % (c+1, ' '.join(map(str, batch)))
    else:
        print 'Case #%d: IMPOSSIBLE' % (c+1)
