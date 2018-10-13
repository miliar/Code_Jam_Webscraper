#!/usr/bin/env python3
T = int(input())
for i in range(T):
    N = int(input())
    while ''.join(sorted(str(N))) != str(N):
        N -= 1
    print("Case #{case}: {result}".format(case=i+1, result=N))
