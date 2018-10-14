#!/usr/bin/python
import sys


if __name__ == '__main__':
    with open(str(sys.argv[1]), 'r') as f:
        cases = int(f.readline().strip())
        for case in range(cases):
            result = 0
            A, B, K = map(int, f.readline().strip().split())
            for i in range(A):
                for j in range(B):
                    if i & j < K:
                        result += 1

            print 'Case #{:}: {:}'.format(case+1, result)






