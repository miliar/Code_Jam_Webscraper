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

class Node:
    def __init__(self, arr):
        if len(arr) == 1:
            self.leaf = True
            self.req = arr[0]
        else:
            self.cost = 1
            l = len(arr) // 2
            self.leaf = False
            self.lft = Node(arr[:l])
            self.rgh = Node(arr[l:])
            self.req = min((self.lft.req, self.rgh.req))
        self.mcost = {}
    def read_cost(self, it, lv):
        if lv==0:
            self.cost = next(it)
        else:
            self.lft.read_cost(it, lv-1)
            self.rgh.read_cost(it, lv-1)
    def min_cost(self, given):
        if given not in self.mcost:
            if self.leaf: return 0
            cwi = (self.cost +
                self.lft.min_cost(given) +
                self.rgh.min_cost(given))
            if given == self.req:
                self.mcost[given] = cwi
            else:
                cwo = (self.lft.min_cost(given+1) +
                    self.rgh.min_cost(given+1))
                self.mcost[given] = min((cwi, cwo))
        return self.mcost[given]

## Calculation
print("Calculation...")
with open(TASK+".in") as infile:
    with open(TASK+".out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            P = int(infile.readline())
            tree = Node( [int(s) for s in infile.readline().split()] )
            for i in range(P):
                tree.read_cost(iter( (int(s) for s in infile.readline().split()) ), P-i-1)
            # Perform all nessesary calculation
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=tree.min_cost(0)))
print("Calculation done.")
