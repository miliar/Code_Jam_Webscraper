#!/usr/bin/env python

import sys
import sortedcontainers


def solve(N, K):
    sl = sortedcontainers.SortedList([N])
    
    for i in xrange(0, K):
        max_space = sl.pop()
        Ls = max_space/2
        Rs = (max_space-1)/2
        sl.add(Ls)
        sl.add(Rs)

    return max(Ls, Rs), min(Ls, Rs)


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        n_testcases = int(fin.readline().strip())
        
        for i_testcase in xrange(1, n_testcases + 1):
            line = fin.readline().strip()
            
            # Parse input line
            #input = map(int, line.split())
            N, K = map(int, line.split())
            
            # Solve
            max_val, min_val = solve(N, K)
            
            # Write solution
            fout.write('Case #{}: {} {}\n'.format(i_testcase, max_val, min_val))


if __name__ == '__main__':
    main()