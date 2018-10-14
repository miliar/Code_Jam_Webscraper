from math import pi

def area(a):
    return a[0] * a[1] * 2 * pi

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    p = []
    p = [[int(x) for x in input().split()] for _ in range(n)]
    a = sorted(p, reverse=True)
    ra = area(a[0]) + (a[0][0]**2)*pi
    a = sorted(a[1:], key=area, reverse=True)
    ra += sum([area(x) for x in a[:k-1]])
    p = sorted(p, key=area, reverse=True)[:k]
    rad = max([x[0] for x in p])
    rp = rad*rad*pi + sum([area(x) for x in p])

    print("Case #{}: {}".format(str(tc), str(max(ra, rp))))
