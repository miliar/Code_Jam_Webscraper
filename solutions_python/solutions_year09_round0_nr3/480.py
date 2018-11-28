import sys

def solve(line, lookfor):
    if not lookfor:
        return 1
    if not line:
        return 0

    res = 0

    for i, c in enumerate(line):
        if c == lookfor[0]:
            res += solve(line[i+1:], lookfor[1:])

    return res


N = int(raw_input())

lookfor = 'welcome to code jam'

for case in xrange(N):
    line = sys.stdin.readline().strip('\n')
    res = solve(line, lookfor)
    print 'Case #%d: %04d' % (case+1, res)
