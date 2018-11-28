import os
import sys
import numpy as np
from scipy.optimize import bisect

def solve_aux(N, K, hs):
    return np.sum(np.sort(hs)[-K:]) if K > 0 else 0
def solve(N, K, rs, hs):
    order = np.argsort(rs)[::-1]
    hs = hs[order]
    rs = rs[order]
    hs = 2*np.pi*np.multiply(rs, hs)
    areas = np.zeros(N)
    for i in range(N):
        height = hs[i]
        height += solve_aux(N, K - 1, hs[i+1:])
        areas[i] = np.pi*rs[i]*rs[i] + height
    return max(areas)

if __name__ == '__main__':
    try:
        input = sys.argv[1]
    except:
        input = os.path.join('data', 'input.txt')
    basename, _ = os.path.splitext(input)
    output = basename + '.output'
    with open(input, 'r') as fin:
        with open(output, 'w') as fout:
            num_cases = int(fin.readline())
            for case in range(num_cases):
                fout.write('Case #%d: ' % (case+1))
                line = fin.readline().split(' ')
                N = int(line[0])
                K = int(line[1])
                rs = np.empty(N)
                hs = np.empty(N)
                for i in range(N):
                    line = fin.readline().split(' ')
                    rs[i] = int(line[0])
                    hs[i] = int(line[1])
                res = solve(N, K, rs, hs)
                fout.write('%f\n' % res)
