import numpy as np
from timeit import default_timer as timer

def solve(D, k, s):
    maxtime = np.max((D - k) / s)
    v = D / maxtime
    return v


if __name__ == '__main__' :
    start = timer()
    out_lines = []
    filename = 'A-large'
    with open(filename + '.in', 'r') as f:
        T = int(f.readline())
        for t in range(1, T+1) :
            # Read a case
            dest, n = [int(x) for x in f.readline().split()]
            data = np.empty((2,n))
            for i in range(n):
                data[:, i] = [int(x) for x in f.readline().split()]
            
            # Solve
            solution = solve(dest, data[0], data[1])                                
            out = 'Case #{}: {:.7f} \n'.format(t, solution)
            out_lines.append(out)
            # Print
            print(out),
            
    with open(filename + '.out', 'w') as fout:
        fout.writelines(out_lines)

    elapsed = timer() - start
    print('Elapsed time: %g' % elapsed)
            
