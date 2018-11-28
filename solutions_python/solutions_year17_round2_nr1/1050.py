#!/usr/bin/env python

import sys

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        n_testcases = int(fin.readline().strip())
        
        for i_testcase in xrange(1, n_testcases + 1):
            line = fin.readline().strip()
            
            # Parse input line
            #input = map(int, line.split())
            D, N = map(int, line.split())
            
            times = []
            for i in xrange(N):
                line = fin.readline().strip()
                K, S = map(int, line.split())
                times.append((D - K) / float(S))
            
            # Write solution
            fout.write('Case #{}: {:.6f}\n'.format(i_testcase, D / max(times)))


if __name__ == '__main__':
    main()