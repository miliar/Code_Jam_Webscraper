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
            rows, cols = (int(s) for s in infile.readline().split())
            field = [[c for c in infile.readline().strip()] for i in range(rows)]
            ans = 'Impossible'
            for i in range(rows):
                for j in range(cols):
                    if field[i][j] != '#': continue
                    field[i][j] = '/'
                    try:
                        if field[i+1][j] == '#': field[i+1][j] = '\\'
                        else: break
                        if field[i][j+1] == '#': field[i][j+1] = '\\'
                        else: break
                        if field[i+1][j+1] == '#': field[i+1][j+1] = '/'
                        else: break
                    except IndexError: break
                else: continue
                break
            else:
                ans = '\n'.join(''.join(r) for r in field)
            # Perform all nessesary calculation
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data='\n'+ans))
print("Calculation done.")
