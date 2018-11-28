import sys
import math
from collections import Counter

def solve(P, gs):
    gs = Counter(g%P for g in gs)
    ans = gs[0]
    gs[0] = 0

    if P == 2:
        ans += int(math.ceil(gs[1] / 2))
    elif P == 3:
        n = min(gs[1], gs[2])
        ans += n
        gs[1] -= n
        gs[2] -= n
        if gs[1] > 0:
            ans += int(math.ceil(gs[1] / 3))
        elif gs[2] > 0:
            ans += int(math.ceil(gs[2] / 3))
    '''
    for i in range(1, int(P//2+1)):
        # how many ways can combinations end up with a new state where someone gets all fresh packs
        n = min(gs[i], gs[P-i])
        if P-i != i:
            ans += n
            gs[i] -= n
            gs[P-i] -= n
        else:
            ans += n//2
            gs[i] -= n//2

    if sum(gs) > 0:
        ans += 1

    while sum(gs) > 0:
        curr = 
'''

    return ans

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    T = int(lines[0])
    i = 1
    for t in range(1,T+1):
        _, P = (int(x) for x in lines[i].split())
        gs = [int(x) for x in lines[i+1].split()]
        i += 2
        print('Case #{}: {}'.format(t, solve(P, gs)))
