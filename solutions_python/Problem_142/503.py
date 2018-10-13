from itertools import groupby
import numpy as np 

t = int(input())

for i in range(t):
    n = int(input())

    inputs = [input() for _ in range(n)]

    groups = [list(groupby(code)) for code in inputs]
    keys = [''.join([c[0] for c in group]) for group in groups]

    if len(set(keys)) != 1:
        print("Case #%i: Fegla Won" % (i+1))

    else:
        zipped_lengths = np.array([[len(list(cgen)) for c, cgen in groupby(input)] for input in inputs]).T
        total = sum([np.sum(np.abs(np.round(np.mean(distrib)) - distrib)) for distrib in zipped_lengths])
        print("Case #%i: %i" % (i+1, int(total)))
