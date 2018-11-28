import fileinput
from collections import Counter

import sys


def read_input():
    # gets next line from the file specified as argument or stdin
    # useful to debug within PyCharm, because you can't redirect stdin :-(
    # first time, initialize a function attribute (it's like a static local function in C++)
    # that will keep state across invocations
    if not hasattr(read_input, 'input'):
        read_input.input = fileinput.input()
    return read_input.input.next().strip()


def split(N):
    # funciona para pares e impares
    return [(N+1)/2-1, N/2]

assert split(3) == [1,1]
assert split(10)== [4,5]
assert split(11) == [5,5]

def solve(N,K):
    segments = [N]
    for i in range(0, K-1):
        segments = split(segments[-1]) + segments[:-1]
        segments = sorted(segments)

    # print segments[-1]
    return sorted(split(segments[-1]))

def solve2(N,K):
    segments = [N]
    c = Counter(segments)
    i = 0
    while i < K:
        largest_segment = sorted(c.keys())[-1]
        s1,s2 = split(largest_segment)
        if c[largest_segment] < K-i:
            i+= c[largest_segment]
            c[s1] += c[largest_segment]
            c[s2] += c[largest_segment]
            del c[largest_segment]
        else:
            return sorted(split(largest_segment))

    # print segments[-1]
    return sorted(split(sorted(c.keys())[-1]))


def solve3(N,K):
    return sorted(split( N/K ))

def solvex(N,K):
    stalls = [True] + [False] * N + [True]

    for i in range(0,K):
        # one person enters
        L = [None] * (N + 2)
        R = [None] * (N + 2)
        left = 0
        right = N+1
        for s in range(0,N+2):
            if not stalls[s]:
                L[s] = s - left - 1
            else:
                left = s
        for s in range(N+1,0,-1):
            if not stalls[s]:
                R[s] = right - s - 1
            else:
                right = s
        # print L
        # print R
        minLR = [ min(l,r) for l,r in zip(L,R)]
        maxLR = [ max(l,r) for l,r in zip(L,R)]
        # print minLR
        # print maxLR

        maxMinLR = -1
        maxMaxLR = -1
        chosen = -1
        for i in range(1,N+1):
            if minLR[i] is None:
                continue

            if minLR[i] > maxMinLR:
                maxMinLR = minLR[i]
                maxMaxLR = maxLR[i]
                chosen = i
            elif minLR[i] == maxMinLR:
                if maxLR[i] > maxMaxLR:
                    chosen = i
                    maxMaxLR = maxLR[i]
        stalls[chosen] = True

    # print stalls
    return maxMaxLR, maxMinLR


if __name__ == "__main__":
    T = int(read_input())
    for i in xrange(1, T+1):
        # sys.stderr.write('%d\n' % (i,))
        N, K = read_input().split()
        N = int(N)
        K = int(K)
        # z,y = solve3(N,K)
        # z,y = solve(N,K)
        z2,y2 = solve2(N,K)
        print("Case #%d: %d %d" % (i, y2, z2))


