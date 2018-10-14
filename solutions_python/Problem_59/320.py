import os

T = int(raw_input())
for case in xrange(1, T + 1):
    N, M = map(int, raw_input().split())

    new_paths = {'/': {}}

    count = 0

    def build_paths(p):
        count = 0
        x = []
        while 1:
            rest, final = os.path.split(p)
            x.append(final)
            if rest == '/':
                break
            p = rest
        start = new_paths
        startp = '/'
        while x:
            e = x.pop()
            if e not in start[startp]:
                count += 1
                start[startp].update({e: {}})
            start = start[startp]
            startp = e
        return count

    for _ in xrange(N):
        p = raw_input()
        build_paths(p)

    for _ in xrange(M):
        p = raw_input()
        count += build_paths(p)

    print "Case #%d: %d" % (case, count)
