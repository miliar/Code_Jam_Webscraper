import itertools as it
import numpy as np
from sys import stdin

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

N = int(next(stdin))
lawns = []
for i in range(N):
    n,m = map(int, next(stdin).split())
    lawn = []
    for _ in range(n):
        lawn.append(list(map(int, next(stdin).split())))
    lawns.append(lawn)

def can(lawn):
    if len(set(lawn.flatten())) == 1:
        return 'YES'
    n,m = lawn.shape
    low = lawn.min()
    for i in range(n):
        for j in range(m):
            if lawn[i,j] == low:
                if not (all(lawn[i,:] == low) or all(lawn[:,j] == low)):
                    return 'NO'
    lawn[lawn == low] += 1
    return can(lawn)

for i,lawn in enumerate(lawns):
    print 'Case #%d: %s' % (i+1, can(np.array(lawn)))
