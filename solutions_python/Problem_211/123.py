def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        u = float(raw_input())
        p = [float(s) for s in raw_input().split(" ")]

        print "Case #{}: {}".format(i, solve(n, k, u, p))


def solve(n, k, u, p):
    p.sort(reverse=True)

    r = 1
    while len(p) > 1:
        z = len(p)
        if (sum(x for i, x in enumerate(p) if i > 0) + u) / (z - 1) >= p[0]:
            return r * ((sum(p) + u) / z) ** z
        r *= p[0]
        p = p[1:]

    return r * (p[0] + u)



if __name__ == '__main__':
    main()
