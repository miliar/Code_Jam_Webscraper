import os
import sys
import numpy as np
from scipy.optimize import bisect

def f(t, ks, ss):
    return min(ks + ss*t)

def solve(D, ks, ss):
    t = bisect(lambda t: f(t, ks, ss) - D, 0, 1e10)
    return D / t

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
                D = int(line[0])
                N = int(line[1])
                ks = np.empty(N)
                ss = np.empty(N)
                for i in range(N):
                    line = fin.readline().split(' ')
                    ks[i] = int(line[0])
                    ss[i] = int(line[1])
                res = solve(D, ks, ss)
                fout.write('%f\n' % res)
