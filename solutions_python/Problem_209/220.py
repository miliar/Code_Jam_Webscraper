import sys
import math
import heapq
from collections import deque
import random

def get_toks(instrm):
    return instrm.readline().rstrip().split()

def get_ints(instrm):
    return [int(s) for s in get_toks(instrm)]
 
def parse(instrm):
    n, k = get_ints(instrm)
    ps = []
    for _ in range(n):
        ps.append(get_ints(instrm))
    return ps, k

def rh_to_score(rh):
    r, h = rh
    return r + h
    
def solve(case):
    ps, k = case
    ps = [(math.pi*r*r, math.pi*2*r*h) for (r, h) in ps]
    ps = sorted(ps)[::-1]
    scores = [[None]*len(ps) for _ in range(len(ps))]
    best = 0
    for i in range(len(ps)):
        curr = ps[i][0] + solve_rec(ps, scores, i, k)
        if curr > best:
            best = curr
    return best

    
def solve_rec(ps, scores, i, k):
    k = min(k, len(ps) - i)
    if k == 0: return 0
    if scores[i][k-1] is None:
        r, h = ps[i]
        best = 0
        for i2 in range(i+1, len(ps)):
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
