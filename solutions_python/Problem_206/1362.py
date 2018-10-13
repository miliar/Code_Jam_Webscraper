#!/usr/bin/python2.7

import numpy as np

def solve_one(D, N, K, S):
    T = (D - K) / S
    cruse_speed = D / T.max()
    return str(cruse_speed)

def main():
    T = int(raw_input())
    for case in xrange(1, T+1):
        D, N = map(int, raw_input().split())
        K = np.empty(N)
        S = np.empty(N)
        for hourse_i in xrange(N):
            K[hourse_i], S[hourse_i] = map(int, raw_input().split())
        print "Case #{}: {}".format(case, solve_one(D, N, K, S))
            
if __name__ == '__main__':
    main()
