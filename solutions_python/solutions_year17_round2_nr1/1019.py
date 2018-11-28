#! /bin/python
test = 0
t = int(input())
while test < t:
    test = test + 1
    d, n = map(int, input().split())
    longest = -1
    for i in range(n):
        k, s = map(int, input().split())
        if longest == -1:
            longest = d / ((d-k)/s)
        longest = min(longest, d / ((d-k)/s))
    print("Case #%d: %.6f" % (test, longest))
