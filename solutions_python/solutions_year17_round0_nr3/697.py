from collections import defaultdict


def split(n):
    return n//2, n - n//2 - 1

for j in range(int(input())):
    N, K = [int(x) for x in input().split()]
    d = defaultdict(lambda: defaultdict(int))
    d[0][N] = 1
    l = 1
    while 2**l-1 < K:
        for val in d[l-1].keys():
            x1, x2 = split(val)
            d[l][x1] += d[l-1][val]
            d[l][x2] += d[l-1][val]
        l += 1
    l = 0
    while 2**(l+1)<= K:
        l += 1
    remain = K - 2**l
    li = sorted(d[l].keys(), reverse=True)
    i = 0
    while remain >= d[l][li[i]]:
        remain -= d[l][li[i]]
        i += 1
    x1, x2 = split(li[i])
    print("Case #"+str(j+1)+":", x1, x2)
