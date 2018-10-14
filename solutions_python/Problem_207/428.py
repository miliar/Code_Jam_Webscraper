R, O, Y, G, B, V = range(6)
LETTERS = list("ROYGBV")


def compatible(c1, c2):
    if c1 == R:
        return c2 not in (R, O, V)
    elif c1 == O:
        return c2 not in (R, O, Y)
    elif c1 == Y:
        return c2 not in (O, Y, G)
    elif c1 == G:
        return c2 not in (G, Y, B)
    elif c1 == B:
        return c2 not in (B, G, V)
    elif c1 == V:
        return c2 not in (V, B, R)


def best_neigh(ccounts, c):
    if c == V:
        neighs = [Y]
    elif c == G:
        neighs = [R]
    elif c == O:
        neighs = [B]
    elif c == R:
        neighs = [Y, B, G]
    elif c == Y:
        neighs = [R, B, V]
    else:
        neighs = [R, Y, O]

    return sorted([(ccounts[n], n) for n in neighs])[-1]


def sol(n, counts):
    condition = (
        counts[V] > 2 * counts[Y] or
        counts[G] > 2 * counts[R] or
        counts[O] > 2 * counts[B]
    )
    if condition:
        return "IMPOSSIBLE"

    for c in (R, O, Y, G, B, V):
        if counts[c] == 0:
            continue
        circular = [None for _ in xrange(n)]
        ccounts = counts[::]
        circular[0] = c
        ccounts[c] -= 1
        for i in xrange(1, n):
            ncount, ncolor = best_neigh(ccounts, circular[i - 1])
            if ncount == 0:
                break
            circular[i] = ncolor
            ccounts[ncolor] -= 1
        if circular[-1] is not None and compatible(circular[-1], circular[0]):
            return "".join(map(lambda x: LETTERS[x], circular))

    return "IMPOSSIBLE"


def show(i, val):
    print "Case #%s: %s" % (i, val)


if __name__ == "__main__":
    T = int(raw_input().strip())

    for i in xrange(1, T + 1):
        tmp = map(int, raw_input().strip().split())
        n = tmp[0]
        counts = tmp[1:]
        show(i, sol(n, counts))


