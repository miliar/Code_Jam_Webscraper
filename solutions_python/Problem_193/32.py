# D
import sys
import itertools

#sys.stdin = open("small.in", "rt")
#sys.stdout = open("small.out", "wt")
sys.stdin = open("D-small-attempt0.in", "rt")
sys.stdout = open("D-small-attempt0.out", "wt")
#sys.stdin = open("D-large.in", "rt")
#sys.stdout = open("D-large.out", "wt")


def fill(perm, busy):
    if not perm:
        return True

    found = False
    for idx, val in enumerate(perm[0]):
        if val == '1' and not busy[idx]:
            found = True
            busy[idx] = True
            if not fill(perm[1:], busy):
                return False
            busy[idx] = False
    return found


def check(W):
    for perm in itertools.permutations(W):
        busy = [False for i in range(len(W))]
        if not fill(perm, busy):
            return False

    return True


def solve(N, W):
    indices = [(r, c) for c in range(N) for r in range(N)]

    for cost in range(0, N ** 2 + 1):
        for select in itertools.combinations(indices, cost):
            empty = True
            for r, c in select:
                if W[r][c] == '1':
                    empty = False
                    break
            if not empty:
                continue

            for r, c in select:
                W[r][c] = '1'

            if check(W):
                return cost

            for r, c in select:
                W[r][c] = '0'

    assert False

#for i in range(100):
#    solve(4, [list("0000")] * 4)

cases = int(input())
for case_idx in range(cases):
    N = int(input())
    W = [list(input()) for i in range(N)]
    print("Case #{}: {}".format(case_idx + 1, solve(N, W)))
