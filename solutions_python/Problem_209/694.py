import sys
import time
from collections import deque
import math

# Next levels nodes: either we put in the next item or not
def next_levels(N, K, node, items):
    (level, profit, raduis, n) = node
    if len(items) == 0 or level >= len(items) - 1 or n == K:
        return []

    next_level = level + 1
    r, h = items[next_level]

    possibilities = [(next_level, profit, raduis, n)]
    if r >= raduis:
        possibilities.append((next_level, profit + math.pi*r*r - math.pi*raduis*raduis + 2*math.pi*r*h, r, n + 1))

    return possibilities

def branch_n_bound(N, K, R, H):
    max_profit = 0

    items = sorted([(R[j], H[j]) for j in range(N)],
            key=lambda x: x[0], reverse=False)

    node = (-1, 0, 0, 0)
    Q = deque()
    Q.append(node)
    while Q:
        (level, profit, raduis, n) = node = Q.pop()
        if profit > max_profit:
            max_profit = profit

        for child in next_levels(N, K, node, items):
            Q.append(child)

    return max_profit


def solution(N, K, R, H):
    return branch_n_bound(N, K, R, H)

def parser():
    N, K = map(int, input().split())
    R = []
    H = []
    for _ in range(N):
        r, h = map(float, input().split())
        R.append(r)
        H.append(h)

    return N, K, R, H

def main():
    T = int(input())
    total_start = time.time()
    # f = open('output/A-small-attempt0.out')
    for case in range(T):
        case_n = case+1

        # _, _, s = next(f).strip().split()
        # s = float(s)

        start = time.time()
        result = solution(*parser())
        # if s > result: sys.stderr.write('Case #{}: {}\n'.format(case_n, s - result))
        timed = time.time() - start
        print('Case #{}: {}'.format(case_n, result))
        sys.stderr.write('Case #{} [\033[0;32mdone\033[0m] {:.3f}s                                  \n'.format(case_n, timed))
    sys.stderr.write('Total time: {:.3f}s\n'.format(time.time() - total_start))

if __name__ == '__main__':
    main()
