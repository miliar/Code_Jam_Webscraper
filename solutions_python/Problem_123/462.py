#!/usr/bin/env python3
def absorb(A, N, motes):
    if A < 2: return N
    motes.sort(reverse = True)
    ops = []
    while motes:
        ops.append(0)
        while motes[-1] >= A:
            A       += A - 1
            ops[-1] += 1
        A += motes.pop()
    l, add, rem = N, 0, 0
    for n in range(N - 1, -1, -1):
        r = l - n
        if ops[n] + add > r:
            l, add = n, 0
            rem   += r
        else: add += ops[n]
    return add + rem

fin  = open("A-large.in",  "r")
fout = open("A-large.out", "w")
T    = int(fin.readline())
for test in range(1, T + 1):
    A, N  = [int(i) for i in fin.readline().split(" ")]
    motes = [int(i) for i in fin.readline().split(" ")]
    ops   = absorb(A, N, motes)
    fout.write("Case #{0}: {1}\n".format(test, ops))
fin.close()
fout.close()
