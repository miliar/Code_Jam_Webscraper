import sys
import itertools
from collections import defaultdict


def gcd(a, b):
    res = (a if b == 0 else gcd(b, a % b))
    return res


def lcm(a, b):
    return (a / gcd(a, b)) * b


m = defaultdict(dict)
m[1][1] = 1
m[1][2] = 2
m[1][3] = 3
m[1][4] = 4

m[2][1] = 2
m[2][2] = -1
m[2][3] = 4
m[2][4] = -3


m[3][1] = 3
m[3][2] = -4
m[3][3] = -1
m[3][4] = 2


m[4][1] = 4
m[4][2] = 3
m[4][3] = -2
m[4][4] = -1


def mul(c1, c2):
    global m
    s1 = 1
    s2 = 1
    if c1 < 0:
        s1 = -1
        c1 = -c1
    if c2 < 0:
        s2 = -1
        c2 = -c2
    return s1 * s2 * m[c1][c2]


def to_num(c):
    if c == '1':
        return 1
    if c == 'i':
        return 2
    if c == 'j':
        return 3
    if c == 'k':
        return 4


def fold(s):
    return reduce(lambda x, y: mul(x, y), s, 1)


def get_ijk(l):
    ll = l[:]
    curr = 1
    while curr != 4 and ll:
        curr = mul(ll[-1], curr)
        ll.pop()
    if curr != 4:
        return (None, False)

    curr = 1
    while curr != 3 and ll:
        curr = mul(ll[-1], curr)
        ll.pop()
    if curr != 3:
        return (None, False)

    curr = 1
    while curr != 2 and ll:
        curr = mul(ll[-1], curr)
        ll.pop()
    if curr != 2:
        return (None, False)
    return (ll, True)


def main():
    filename = sys.argv[1]
    in_f = open(filename)
    T = int(in_f.readline().strip())

    for t in xrange(T):
        L, X = [int(x) for x in in_f.readline().strip().split()]
        s = [to_num(x) for x in in_f.readline().strip()]
        N = lcm(L, X)
        K = (L * X) / N
        n_s = s * (N / L)

        cnt = 1
        while cnt <= K:
            l, res = get_ijk(n_s * cnt)
            if res:
                break
            cnt += 1
        folded = fold(n_s)
        rr = "NO"
        if res:
            if 1 == fold([folded] * (K - cnt) + l):
                rr = "YES"
        print "Case #{}: {}".format(t + 1, rr)


if __name__ == "__main__":
    main()
