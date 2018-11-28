#!/usr/bin/python2
### Google Code Jam template
## Library
# @memoized
def memoized(func):
    mem = {}
    def wrapped(*args):
        if args not in mem:
            mem[args] = func(*args)
        return mem[args]
    return wrapped

## Setup
# Task letter
TASK="B"

## Input templates
# Line as int
#int(infile.readline())
# Line as many ints
#(int(s) for s in infile.readline().split())

## Precalculation
#print("Precalculation...")
#print("Precalculation done.")

## Calculation
print("Calculation...")
with open(TASK+".in") as infile:
    with open(TASK+".out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            # Read the input
            A = [int(s) for s in infile.readline().split()]
            L, t, N, C = A[0:4]
            A = A[4:]
            time = lambda n: A[n%C]
            pos = 0
            ct = 0
            assert t % 2 == 0
            # Initial calculation
            Nloops = N / C
            Ttotal = 2 * (Nloops * sum(A) + sum(A[:N - Nloops * C]))
            # Stage 1: pre-boost
            looptime = sum(A) * 2
            loops = min(t / looptime, N / C)
            ct += loops * looptime
            pos += loops * C
            while ct + time(pos) * 2 <= t and pos < N:
                ct += time(pos) * 2
                pos += 1
            # Stage 2: initial booster and pre-boosted way
            # We're at star 'pos', the current time is ct
            # So let's calculate how many elements of any given way we need to pass
            from collections import defaultdict
            pathsbylen = defaultdict(lambda: 0)
            loops = (N - pos - 1) / C
            # Complete loops
            for l in A: pathsbylen[l] += loops
            # Incomplete loop
            for i in range(pos + 1, N - loops * C):
                pathsbylen[time(i)] += 1
            # Initial
            pathsbylen[time(pos) - (t - ct) / 2] += 1
            # Calculation
            pathsbylen = [(l, n) for l, n in pathsbylen.items()]
            pathsbylen.sort(reverse=True)
            assert Ttotal == t + sum(l * n * 2 for l, n in pathsbylen)
            assert N == pos + sum(n for l, n in pathsbylen)
            for l, n in pathsbylen:
                cb = min(n, L)
                L -= cb
                Ttotal -= cb * l
                if L == 0: break
            # Perform all nessesary calculation
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=Ttotal))
print("Calculation done.")
















