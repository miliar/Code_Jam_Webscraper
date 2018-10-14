import sys
from decimal import *

def solve(D, horses):
    max_time = None
    for horse in horses:
        remaining = D - horse[0]
        time = Decimal(remaining) / Decimal(horse[1])
        if max_time == None or time > max_time:
            max_time = time
    return Decimal(D) / max_time

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for case in range(T):
        D, N = map(int, sys.stdin.readline().split())
        horses = []
        for horse in range(N):
            K, S = map(int, sys.stdin.readline().split())
            horses.append((K, S))
        print "Case #{}: {:.8f}".format(case + 1, solve(D, horses))
