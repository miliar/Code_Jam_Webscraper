import sys
import math

def solve(s):
    
    claps = 0
    adds = 0
    for i, v in enumerate(s):
        if claps < i:
            rest = i - claps
            claps += rest
            adds += rest
        claps += v

    return adds

if __name__ == '__main__':

    T = int(sys.stdin.readline())

    for t in range(T):
        S, V = sys.stdin.readline().split()

        S = int(S)
        V = map(int, V)
        #print t, S, V
        res = solve(V)
        print "Case #%d: %d" % ((t+1), res)
