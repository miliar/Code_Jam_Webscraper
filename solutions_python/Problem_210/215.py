import sys
import math
import heapq
from collections import deque
import random
import sys

sys.setrecursionlimit(10000)

def get_toks(instrm):
    return instrm.readline().rstrip().split()

def get_ints(instrm):
    return [int(s) for s in get_toks(instrm)]
 
def parse(instrm):
    ac, aj = get_ints(instrm)
    acts = []
    for _ in range(ac):
        s, e = get_ints(instrm)
        acts.append((s, e, 0))
    for _ in range(aj):
        s, e = get_ints(instrm)
        acts.append((s, e, 1))
    return acts

def solve(acts):
    if len(acts) == 0:
        return 2
    acts.sort()
    sl, el, wl = acts[0]
    acts.append((sl + 720*2, el + 720*2, wl))
    ts = [0, 0]; ints = [[], []]; nexch = 0
    for i, (sa, ea, wa) in enumerate(acts):
        if i == 0: continue
        sb, eb, wb = acts[i-1]
        if wa != wb:
            nexch += 1
            ts[wb] += eb - sb
        else:
            ts[wb] += sa - sb
            ints[wb].append((sa - eb))
    if ts[0] > ts[1]:
        t = ts[0]
        i = ints[0]
    else:
        t = ts[1]
        i = ints[1]
    i = sorted(i)
    while t > 720:
        delta = i.pop()
        t -= delta
        nexch += 2
    return nexch

    
def solve_rec(ps, scores, i, k):
    if k == 0: return 0
    if scores[i][k-1] is None:
        r, h = ps[i]
        best = 0
        for i2 in range(i+1, len(ps) - k + 2):
            best = max(best, solve_rec(ps, scores, i2, k-1))
        scores[i][k-1] = h + best
    return scores[i][k-1]

if __name__ == "__main__":
    with open(sys.argv[1]) as instrm:
        n = int(instrm.readline())
        for i in range(n):
            case = parse(instrm)
            ans = solve(case)
            print("Case #{}: {}".format(i+1, ans))
