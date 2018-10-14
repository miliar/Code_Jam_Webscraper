#!/usr/bin/python2
## Setup
# Task letter
TASK="C"

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
            infile.readline()
            values = [int(s) for s in infile.readline().split()]
            poss = (reduce(lambda x, y: x ^ y, values) == 0)
            if not poss: ans = "NO"
            else: ans = sum(values) - min(values)
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=ans))
print("Calculation done.")
