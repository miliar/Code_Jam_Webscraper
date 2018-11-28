def join(str1, str2):
    i = 0

    res = ""

    for i in xrange(max(len(str1), len(str2))):
        if i < len(str1):
            res += str1[i]
        if i < len(str2):
            res += str2[i]

    return res


def solve(N, R, O, Y, G, B, V):
    Rstr = 'R' * R
    Ystr = 'Y' * Y
    Bstr = 'B' * B

    if R > Y:
        RY = join(Rstr, Ystr)[::-1]
    else:
        RY = join(Ystr, Rstr)[::-1]
    res = join(Bstr, RY)

    cur = res[-1]
    for c in res:
        if c == cur:
            return 'IMPOSSIBLE'
        cur = c
    return res


T = int(raw_input())

for i in xrange(T):
    N, R, O, Y, G, B, V = [int(x) for x in raw_input().split()]

    print 'Case #%d: %s' % (i + 1, solve(N, R, O, Y, G, B, V))
