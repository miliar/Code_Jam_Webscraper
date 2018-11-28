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
TASK="C"
# This is C-small only

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
            # Perform all nessesary calculation
            N, L, H = (int(s) for s in infile.readline().split())
            notes =  [int(s) for s in infile.readline().split()]
            for freq in range(L, H+1):
                for note in notes:
                    if note % freq and freq % note:
                        break
                else:
                    tune = freq
                    break
            else:
                tune = "NO"
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=tune))
print("Calculation done.")
