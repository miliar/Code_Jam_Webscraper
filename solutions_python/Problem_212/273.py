import sys
import itertools

def read_line(as_what=int):
    return [as_what(s) for s in raw_input().split()]

def find(G, P, currP):
    best = P
    bestIdx = -1
    for j, i in enumerate(G):
        if (i + currP) % P < best:
            best = (i + currP) % P
            bestIdx = j
    return bestIdx, best

def solve(G, P, R):
    curr = 0
    total = 0
    while len(G) > 0:
        if curr > 0:
            total += 1
        idx, curr = find(G, P, curr)
        G[idx:idx+1] = []
    return R - total

T, = read_line()
for i in range(1, T + 1):
    R, P = read_line()
    G = [x % P for x in read_line()]
    print("Case #{}: {}".format(i, solve(G, P, R)))
