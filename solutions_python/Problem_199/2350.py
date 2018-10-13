#!/usr/bin/env python
from sys import stdin


def process():
    line = stdin.readline().split(" ")
    S = list(line[0])
    K = int(line[1])
    flips = 0
    for i in range(len(S) - K + 1):
        if S[i] == '-':
            flips += 1
            for j in range(i, i + K):
                S[j] = '+' if S[j] == '-' else '-'
    if '-' in S:
        return "IMPOSSIBLE"
    else:
        return flips

def main():
    N = int(stdin.readline())
    for i in range(N):
        print("Case #{}: {}".format(i + 1, process()))

if __name__ == '__main__':
    main()


