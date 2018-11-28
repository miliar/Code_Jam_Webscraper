#!/usr/bin/env python

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    S = str(N)[::-1]
    LIMIT = len(S) - 1
    flipped = False
    for d in range(len(S)):
        S = str(N)[::-1]
        LIMIT = len(S) - 1
        for i in range(LIMIT):
            if S[i] < sorted(S[i+1:])[::-1][0]:
                if S[i] == '0':
                    N -= (10 ** i)
                else:
                    N -= (10 ** i) * (1 + int(S[i]))
                S = str(N)[::-1]
                flipped = True
            # print("N = {}".format(N))
            if len(S)-1 != LIMIT:
                break

        if flipped:
            S = str(N)[::-1]
            LIMIT = len(S) - 1
            for i in range(LIMIT):
                if S[i] < sorted(S[i+1:])[::-1][0]:
                    N += (10 ** i) * (9 - int(S[i]))
                    S = str(N)[::-1]
                if len(S)-1 != LIMIT:
                    break

    print("Case #{}: {}".format(t, N))
