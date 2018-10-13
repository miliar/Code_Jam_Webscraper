# https://code.google.com/codejam/contest/5304486/dashboard

import sys

def solve(D, N, horses):
    t = [float(D - K)/S for K, S in horses]
    return D/max(t)

if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    for i in range(T):
        D, N = map(int, f.readline().split())
        horses = [map(int, f.readline().split()) for j in range(N)]
        print "Case #"+str(i+1)+": "+str(solve(D, N, horses))
