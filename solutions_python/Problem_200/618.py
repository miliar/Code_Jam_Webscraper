#! /bin/python

from sys import stdin


T = int(stdin.readline().strip())

for t in range(T):
    N = [int(x) for x in stdin.readline().strip()]

    for i in range(len(N) -2, -1, -1):
        if N[i] > N[i+1]:
            N[i] = N[i] - 1
            if N[i] == -1:
                N[i] = 9
            N[i+1:] = [9]*len(N[i+1:])

    print("Case #{}: {}".format(t+1, int("".join([str(x) for x in N]))))
