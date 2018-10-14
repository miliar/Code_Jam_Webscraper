#! /usr/bin/python3

T = int(input())
for test in range(1, T+1):
    D, N = [int(x) for x in input().strip().split(' ')]
    min_t = -1
    for _ in range(N):
        k, s = [int(x) for x in input().strip().split(' ')]
        t = (D - k)/s
        if t > min_t:
            min_t = t
    r = D / min_t
    print('Case #%d: %s' % (test, r))