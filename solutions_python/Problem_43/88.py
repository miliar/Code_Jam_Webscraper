def count_unique(line):
    seen = {}
    for c in line:
        seen[c] = 0
    return len(seen.keys())


def solve(line):
    base = count_unique(line)
    if base == 1:
        base = 2
    assign = {}

    assign[line[0]] = 1
    v = 0
    for c in line[1:]:
        if c not in assign:
            if v == 1: v = 2
            assign[c] = v
            v += 1

    res = 0

    for c in line:
        res = res * base + assign[c]

    return res


T = int(raw_input())

for t in xrange(T):
    line = raw_input()
    print 'Case #%d: %d' % (t+1, solve(line))
