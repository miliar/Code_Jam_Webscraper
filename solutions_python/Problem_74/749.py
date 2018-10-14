import sys

def solve(bs):

    def other(c):
        return (set(['O', 'B']) - set(c)).pop()

    res = 0

    loc = {'O': 1, 'B': 1}
    slack = {'O': 0, 'B': 0}

    for b in bs:
        c = b[0]
        l = int(b[1])
        t = abs(loc[c] - l)
        t -= slack[c]
        t = max(t, 0)
        o = other(c)
        slack[o] += t + 1
        slack[c] = 0
        loc[c] = l
        res += t + 1

    return res


T = int(raw_input())

for t in xrange(T):
    line  = sys.stdin.readline().strip()
    spl = line.split(' ')[1:]

    bs = []
    for i in xrange(0, len(spl), 2):
        bs.append((spl[i], spl[i + 1]))

    print 'Case #%d: %d' % (t+1, solve(bs))
