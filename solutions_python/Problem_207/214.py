def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, r, o, y, g, b, v = [int(s) for s in raw_input().split(" ")]

        print "Case #{}: {}".format(i, solve(n, r, o, y, g, b, v))


def solve(n, r, o, y, g, b, v):
    if o != 0 or g != 0 or v != 0:
        return 'IMPOSSIBLE'

    a = [[r, 'R'], [y, 'Y'], [b, 'B']]
    if max(a)[0] > n / 2:
        return 'IMPOSSIBLE'

    a.sort(reverse=True)
    res = []

    while min(a)[0] > 0 and (a[0][0] != a[1][0] + a[2][0]):
        res.append(a[0][1])
        res.append(a[1][1])
        res.append(a[2][1])
        a[0][0] -= 1
        a[1][0] -= 1
        a[2][0] -= 1

    for i in range(a[2][0]):
        res.append(a[0][1])
        res.append(a[2][1])
    a[0][0] -= a[2][0]
    a[2][0] = 0

    for i in range(a[1][0]):
        res.append(a[0][1])
        res.append(a[1][1])

    return ''.join(res)


if __name__ == '__main__':
    main()
