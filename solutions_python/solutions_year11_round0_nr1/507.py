#!/usr/bin/python2
## Setup
# Task letter
TASK="A"

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
            prog = infile.readline().split()
            prog = zip(prog[1::2], (int(i) for i in prog[2::2]))
            print(prog)
            bp = 1
            bt = 0
            op = 1
            ot = 0
            for r, c in prog:
                if r == 'B':
                    bt = max(bt + abs(c-bp) + 1, ot + 1)
                    bp = c
                if r == 'O':
                    ot = max(ot + abs(c-op) + 1, bt + 1)
                    op = c
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=max(ot,bt)))
print("Calculation done.")
