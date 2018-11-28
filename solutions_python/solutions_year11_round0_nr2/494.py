from collections import defaultdict

def parse(l):
    e = iter(l.split())
    C = int(e.next())
    bases = {}
    for _ in xrange(C):
        s = e.next()
        bases[(s[0], s[1])] = s[2]
        bases[(s[1], s[0])] = s[2]
    D = int(e.next())
    opposed = {}
    for _ in xrange(D):
        s = e.next()
        opposed.setdefault(s[0], []).append(s[1])
        opposed.setdefault(s[1], []).append(s[0])
    N = int(e.next())
    invoke = e.next()
    assert(len(invoke) == N)
    return bases, opposed, invoke

def solve(l):
    bases, opposed, invoke = parse(l)
    # print
    # print bases
    # print opposed
    r = []
    count = defaultdict(int)
    for e in invoke:
        r.append(e)
        count[e] += 1

        if len(r) < 2:
            continue

        e1 = r[-1]
        e2 = r[-2]
        pair = (e1, e2)
        new = bases.get(pair)
        if new:
            # Magic base found, transform to non-base element
            count[e1] -= 1
            count[e2] -= 1
            count[new] += 1
            r[-2:] = [new]
        else:
            # Is the new element opposed to some element already in the list?
            for o in opposed.get(r[-1], []):
                if count[o]:
                    r = []
                    count = defaultdict(int)

    return r

if __name__ == '__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        e = solve(raw_input())
        def f():
            return '[' + ', '.join(e) + ']'
        print 'Case #%d: %s' % (i, f())
