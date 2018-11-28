import math

t = int(input())
for i in range(1, t + 1):
    d, n = input().split(" ")
    d = int(d)
    n = int(n)

    max_time = -math.inf

    for j in range(0, n):
        k, s = input().split(" ")
        k = int(k)
        s = int(s)
        max_time = max(max_time, (d - k) / s)

    print("Case #" + str(i) + ": " + str("{0:.6f}".format(d / max_time)))