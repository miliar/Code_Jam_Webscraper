from math import sqrt, trunc
a = [0] * 1001
a[0] = 1
for x in range(1, 1001):
    y = sqrt(x)
    if y == trunc(y):
        s1 = str(x)
        s2 = str(trunc(y))
        if s1 == s1[::-1] and s2 == s2[::-1]:
            a[x] = a[x - 1] + 1
        else:
            a[x] = a[x - 1]
    else:
        a[x] = a[x - 1]
T = int(raw_input())
for t in range(1, T + 1):
    x, y = map(int, raw_input().split())
    print "Case #{0}: {1}".format(t, a[y] - a[x - 1])
