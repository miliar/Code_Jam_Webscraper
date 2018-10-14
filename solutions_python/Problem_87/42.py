if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        X, S, R, t, N = [int(s) for s in raw_input().split()]
        c = []
        for _ in xrange(N):
            b, e, w = [int(s) for s in raw_input().split()]
            c += [(b, e, w)]

        c.sort()

        sections = []
        if c[0][0] > 0:
            sections += [(0, c[0][0], S, R)]
        for i in xrange(len(c)):
            sections += [(c[i][0], c[i][1], S + c[i][2], R + c[i][2])]
            if i > 0 and c[i-1][1] < c[i][0]:
                sections += [(c[i-1][1], c[i][0], S, R)]

        if c[-1][1] < X:
            sections += [(c[-1][1], X, S, R)]

        sections.sort(key=lambda x: x[2])

        res = 0
        for b, e, s, r in sections:
            if t > 0:
                dt = (e - b) / float(r)
                if t >= dt:
                    t -= dt
                else:
                    rd = t * r
                    dt = (e - b - rd) / float(s) + t
                    t = 0
            else:
                dt = (e - b) / float(s)

            res += dt


        print 'Case #%d: %.9f' % (caseno + 1, res)
