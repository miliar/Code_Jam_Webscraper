#!/usr/bin/env python3

T = int(input())

for t in range(1, T+1):
    N = list('000' + input())

    def fix(i):
        if N[i-1] > N[i]:
            N[i-1] = chr(ord(N[i-1]) - 1)
            fix(i-1)
        else:
            for j in range(i + 1, len(N)):
                N[j] = '9'

    for i in range(1, len(N)):
        if N[i-1] > N[i]:
            fix(i)

    while N[0] == '0':
        N = N[1:]

    print("Case #{}: {}".format(t, ''.join(N)))
