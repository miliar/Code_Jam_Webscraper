#!/usr/bin/env python

import fileinput

def tokenizer():
    inp = fileinput.input()
    for line in inp:
        tokens = line.split()
        for tk in tokens:
            yield tk

tokens = tokenizer()

T = int(next(tokens))

def tidy(N):
    n = list(str(N))

    for i in range(1,len(n)):
        if n[i] < n[i-1]:
            d = 0
            for d in range(i, len(n)-1):
                if n[d] != n[d+1]:
                    return d+1
            return max(i,d+1)
    return -1


for case in range(T):
    N = int(next(tokens))

    idx = tidy(N)

    while (idx != -1):
        #print("checking {}".format(N))
        maxidx = len(str(N))-1
        dec = 10**(maxidx-idx)
        #print("nlen: {}, dec: {}, idx: {}".format(maxidx, dec, idx))
        N = N-dec
        idx = tidy(N)

    print("Case #{}: {}".format(case+1, N))
