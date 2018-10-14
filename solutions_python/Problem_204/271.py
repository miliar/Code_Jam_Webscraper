def solve(n, p, r, q):
    res = 0
    print n, p, r, q

    l = [0] * n
    while(max(l) < p):
        l0 = l[0]

    return res


def solve2(p, r, q):
    res = 0
    j = 0
    t = [[], []]
    for i in range(2):
        for j in range(p):
            s = servings(r[i], q[i][j])
            if s:
                t[i].append(s)

    u = [len(v) for v in t]
    i = 0
    j = 0
    while(i < u[0] and j < u[1]):
        xa, xb = t[0][i]
        ya, yb = t[1][j]
        if xb < ya:
            i += 1
            continue
        if xa > yb:
            j += 1
            continue
        # print t[0][i], t[1][j]
        i += 1
        j += 1
        res += 1
    return res


def solve1(p, r, q):
    r0 = r[0]
    res = 0
    for i in range(p):
        s = servings(r0, q[0][i])
        # print s
        if s:
            res += 1
    return res


def servings(r, q):
    # print r, q
    import math
    a = int(math.floor(q / (r * 1.1)))
    b = int(math.ceil(q / (r * 0.9)))
    if a * r * 1.1 < q:
        a += 1
    if b * r * 0.9 > q:
        b -= 1

    if b >= a:
        return (a, b)
    else:
        return None


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, p = [int(c) for c in raw_input().split(" ")]
        r = [int(c) for c in raw_input().split(" ")]
        q = []
        for j in xrange(0, n):
            q.append(sorted([int(c) for c in raw_input().split(" ")]))
        if n == 1:
            sol = solve1(p, r, q)
        if n == 2:
            sol = solve2(p, r, q)
        print "Case #{}: {}".format(i, sol)


if __name__ == "__main__":
    main()
