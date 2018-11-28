from functools import reduce
for t in range(int(input())):
    n, k = map(int, input().split())
    u = float(input())
    p = list(map(float, input().split()))

    p.sort()
    p.append(1.0)

    for i in range(1, len(p)):
        g = p[i]-p[i-1]
        h = g*i
        h = min(h, u)
        u -= h
        for j in range(i):
            p[j] += h/i

    ans = reduce(lambda a,b:a*b, p[:-1])
    print('Case #{}: {}'.format(t+1, ans))