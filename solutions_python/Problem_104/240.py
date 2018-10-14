import itertools

def solve(S):
    for n in xrange(1, len(S)):
        for c in itertools.combinations(S, n):
            s0 = sum(c)
            d = [i for i in S if i not in c]
            for m in xrange(1, len(d) + 1):
                for cc in itertools.combinations(d, m):
                    s1 = sum(cc)
                    if s0 == s1:
                        return c, cc

if __name__ == '__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        S = set([int(e) for e in raw_input().split()][1:])
        sets = solve(S)
        if not sets:
            r = ['Impossible']
        else:
            r = [' '.join(str(i) for i in sets[0]),
                 ' '.join(str(i) for i in sets[1])]
        print 'Case #%d:' % i
        for l in r:
            print l
