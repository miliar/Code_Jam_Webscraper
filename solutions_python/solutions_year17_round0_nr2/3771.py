import os
import sys
import numpy as np

def solve_rec(N, inf):
    N = str(N)
    if int(N[0]) < inf:
        return -1
    if len(N) == 1:
        return int(N[0])
    for i in reversed(range(inf, int(N[0])+1)):
        res = solve_rec(int(N[1:]), i)
        if res != -1:
            if i < int(N[0]):
                return int(str(i) + '9'*(len(N)-1))
            return int(str(i) + str(res))
    if int(N[0])-1 < inf:
        return -1
    return int(str(int(N[0])-1) + '9'*(len(N)-1))

def is_tidy(N):
    N = np.asarray(list(map(int, str(N))))
    if len(np.where(np.diff(N) < 0)[0]) > 0:
        return False
    else:
        return True

def solve(N):
    for n in reversed(range(1, N+1)):
        if is_tidy(n):
            return n

if __name__ == '__main__':
    try:
        input = sys.argv[1]
    except:
        input = os.path.join('data', 'input.txt')
    output = os.path.join('data', 'output.txt')
    with open(input, 'r') as fin:
        with open(output, 'w') as fout:
            num_cases = int(fin.readline())
            for case in range(num_cases):
                fout.write('Case #%d: ' % (case+1))
                line = fin.readline()
                N = int(line)
                res = solve(N)
                fout.write(str(res) + '\n')
