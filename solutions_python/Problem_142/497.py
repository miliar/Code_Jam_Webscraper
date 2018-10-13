def conv(s):
    r = []
    cur = None
    for c in s:
        if c != cur:
            r.append((c, 1))
            cur = c
        else:
            r[-1] = (r[-1][0], r[-1][1] + 1)
    return r


def solve(strs):
    strs = [conv(s) for s in strs]
    L = len(strs[0])
    if any(len(s) != L for s in strs):
        return 'Fegla Won'
    for i in xrange(L):
        if any(s[i][0] != strs[0][i][0] for s in strs):
            return 'Fegla Won'
    moves = 0
    for i in xrange(L):
        total = sum(s[i][1] for s in strs)
        avg = round(total / float(len(strs)))
        moves += sum(abs(s[i][1] - avg) for s in strs)
    return '%d' % moves


def run():
    T = int(raw_input())
    for i in xrange(T):
        N, = [int(x) for x in raw_input().split()]
        strs = []
        for _ in xrange(N):
            strs.append(raw_input().strip())
        r = solve(strs)
        print 'Case #%d:' % (i + 1), r


if __name__ == '__main__':
    run()
