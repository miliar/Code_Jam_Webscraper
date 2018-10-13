import sys
import numpy as np


def solve(N, K, u, p, test_case):
    
    p.sort()
    
    num_eq = 0
    while (num_eq < N) and (abs(p[num_eq] - p[0]) < 1e-8):
        num_eq += 1
    
    while (num_eq < N) and (u > 0):
        inc = min(u / num_eq, p[num_eq] - p[0])
        for i in range(num_eq):
            p[i] += inc
        u -= inc * num_eq
        while (num_eq < N) and (abs(p[num_eq] - p[0]) < 1e-8):
            num_eq += 1
    
    if (num_eq == N) and (u > 1e-8):
        for i in range(N):
            p[i] += u / N
    
    solution = np.prod(p)
    
    print('Case #{}: {}'.format(test_case, solution))


def solve_all(fn):
    
    with open(fn) as f:
        T = int(f.readline().strip())
        for tc in range(1, T+1):
            N, K = [int(x) for x in f.readline().strip().split()]
            u = float(f.readline().strip())
            p = [float(x) for x in f.readline().strip().split()]
            solve(N, K, u, p, tc)


if __name__ == '__main__':
    solve_all(sys.argv[1])