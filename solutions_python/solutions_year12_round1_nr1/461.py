#!/usr/bin/env python2.6

def get_df_ps(ps):
    '''build an array representing the probs that each letter typed is
    the 'deepest' failure, n being no failure, len(dfps) == len(ps) + 1'''
    dfps = [1 - ps[0]]
    cps = ps[0]
    for p in ps[1:]:
        dfps.append((1 - p) * cps)
        cps = cps * p

    return (dfps, cps)

def do_case(a, b, ps):
    (df_ps, cp) = get_df_ps(ps)

    #print df_ps,
    #print cp

    #expected if you keep typing
    kts = [(2 * b - a + 2) * p for p in df_ps] + [(b - a + 1) * cp]
    kte = sum(kts)
    #print kte

    #expected for backspacking n
    bses = []
    df_ps.append(cp)
    #print df_ps
    for i in range(1, a + 1):
        ksg = (b - a + (2 * i) + 1)
        bseg = [ksg * dps for dps in df_ps[-i - 1:]]
        #print bseg
	ksb = ((2 * b) - a + (2 * 1) + 2)
        bseb = [ksb * dps for dps in df_ps[:-i - 1]]
        #print bseb
        bses.append(sum(bseg + bseb))
    
    #expected for enter right away
    rae = b + 2
    #print rae

    return min([kte] + bses + [rae])

if __name__ == '__main__':
    import sys

    input = open(sys.argv[1])

    ct = int(input.readline().strip())
    for i in range(1, ct + 1):
        (a, b) = [int(n) for n in input.readline().strip().split()]
        ps = [float(f) for f in input.readline().strip().split(' ')]

        e = do_case(a, b, ps)
        print 'Case #%i: %.6f' % (i, e)
