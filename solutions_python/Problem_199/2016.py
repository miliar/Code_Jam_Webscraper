## Google CodeJam 2017-04-08 
## Problem A: "Oversized pancake flipper" 
## @author Ylva Jansson

def pcaketolist(pcake):
    res = [0 if s == '-' else 1 if s == '+' else None for s in pcake]
    return res

def flip(pancakes, i, K): 
    for i in range(i,i+K):
        pancakes[i] = int(not pancakes[i])

def flipping(pancakes, K):
    n_pancakes = len(pancakes)
    n_flips = 0
    for i in range(n_pancakes-K+1):
        if pancakes[i] == 0:
            flip(pancakes, i, K)
            n_flips += 1
    
    if 0 in pancakes[-K+1:]:
        return "IMPOSSIBLE"
    else:
        return n_flips
        
# Read input
nT = int(input())  # read a line with a single integer
pancakes = [None]*nT
K = [None]*nT
for i in range(nT):
    pancakes[i], K[i] = input().split() # read a single integer

res = [None]*nT
for i in range(nT):
    res[i] = flipping(pcaketolist(pancakes[i]), int(K[i]))
    
for i in range(1,len(res)+1):
    print('Case #' + str(i) + ": " + str(res[i-1]))
