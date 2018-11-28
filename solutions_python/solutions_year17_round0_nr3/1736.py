import sys
from math import log2, floor, ceil

def solve(N, K):
    left = floor((N - 1) / 2)
    right = ceil((N - 1) / 2)
    if K == 1:
        return right, left
    elif K % 2 == 0:
        return solve(right, K / 2)
    else:
        return solve(left, (K - 1) / 2)

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        T = int(f.readline().strip())
        for case in range(T):
            N, K = (int(i) for i in f.readline().strip().split())
            mx, mn = solve(N, K)
            print('Case #{}: {} {}'.format(case + 1, mx, mn))
