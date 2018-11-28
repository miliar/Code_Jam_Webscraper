if __name__ == '__main__':
    T = int(raw_input())
    for caseno in xrange(T):
        N, pd, pg = [int(s) for s in raw_input().split()]

        res = False
        for i in xrange(1, N + 1):
            if (i * pd) % 100 == 0:
                res = True
                break

        if pg == 100 and pd < 100:
            res = False
        if pg == 0 and pd > 0:
            res = False

        print 'Case #%d: %s' % (caseno + 1, 'Possible' if res else 'Broken')
