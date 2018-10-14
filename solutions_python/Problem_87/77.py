#!/usr/bin/python3

import sys

def read():
    return tuple(map(int, sys.stdin.readline().split()))

T, = read()
for case in range(1, T+1):
    X, S, R, t, N = read()
    seq = sorted([read() for i in range(N)])
    e = seq[0][0] + X - seq[N-1][1]
    for i in range(N-1):
        e += seq[i+1][0] - seq[i][1]
    seq.append((0, e, 0))
    seq = sorted(seq, key=lambda x: x[2])
    ret = 0.0
    for i in range(len(seq)):
        l = seq[i][1] - seq[i][0]
        ss = seq[i][2] + S
        sr = seq[i][2] + R
        if l / sr > t:
            ret += t + (l-sr*t)/ss
            t = 0.0
        else:
            ret += l / sr
            t -= l / sr
    print('Case #{}: {:.9f}'.format(case, ret))
