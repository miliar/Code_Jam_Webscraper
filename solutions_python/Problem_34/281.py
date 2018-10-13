import psyco
psyco.full()

def solve():
    L, D, N = [int(s) for s in raw_input().split()]

    words = []
    for i in xrange(D):
        words += [raw_input()]

    for case in xrange(N):
        s = raw_input()

        pat = []
        p = 0;
        while len(pat) < L:
            if s[0] != '(':
                pat += [s[0]]
                s = s[1:]
            else:
                l = s.find(')')
                pat += [s[1:l]]
                s = s[l+1:]

        res = 0
        for w in words:
            match = True
            for i in xrange(L):
                if not w[i] in pat[i]:
                    match = False
                    break

            if match:
                res += 1

        print 'Case #%d: %d' % (case+1, res)

solve() # so that psyco can do its magic
