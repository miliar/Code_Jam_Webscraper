from math import pi

def b(rh):
    return 2 * rh[0] * rh[1]


def a(n, k, cakes):
    ma = 0
    for j, i in enumerate(cakes):
        ans = i[0] ** 2 + b(i)
        nc = cakes[:j] + cakes[j + 1:]
        nc = list(filter(lambda x: x[0] <= i[0], nc))
        if len(nc) < k - 1:
            continue
        nc = list(map(b, nc))
        nc.sort(key=lambda x: -x)
        nc = nc[:k - 1]
        ans += sum(nc[:k - 1])
        ma = max(ans, ma)
    return ma * pi


if __name__ == "__main__":
    with open("sub-5.in") as fi,\
            open("output", "w") as fo:
        t = int(fi.readline())
        for i in range(1, t + 1):
            n, k = map(int, fi.readline().split())
            cakes = []
            for j in range(n):
                    cakes.append(tuple(map(int, fi.readline().split())))

            fo.write("Case #{0}: {1}\n".format(i, a(n, k, cakes)))
