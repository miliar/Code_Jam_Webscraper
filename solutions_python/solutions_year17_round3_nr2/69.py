import os

def g(lc):
    x1, y1 = lc[0]
    x2, y2 = lc[1]
    if y2 - x1 <= 720: return 2
    if (y1 - x2 + 24 * 60) % (24 * 60) <= 720: return 2
    return 4

def solve2(ac, aj, lc, lj):
    if ac < 2 and aj < 2: return 2
    if ac == 2: return g(lc)
    if aj == 2: return g(lj)
    return 2

def solve(ac, aj, lc, lj):
    gl = [(x, y, 'c') for x, y in lc]
    gl.extend([(x, y, 'j') for x, y in lj])
    gl.sort()
    x, y, z = gl[0]
    gl.append((x + 24 * 60, y + 24 * 60, z))

    dd = []
    for i in xrange(ac + aj):
        x, y, z = gl[i]
        x2, y2, z2 = gl[i + 1]
        if z == z2:
            dd.append((x2 - y, z, i))

    dd.sort()
    cc = sum([y-x for x,y in lc])
    jj = sum([y - x for x, y in lj])

    mm = {}
    comb = 0
    for d,z,i in dd:
        if z == 'c':
            if d <= 12*60 - cc:
                cc += d
                comb += 1
                mm[i]=True
        else:
            if d <= 12*60 - jj:
                jj += d
                comb += 1
                mm[i] = True
    hh = 0
    for i in xrange(ac + aj):
        x, y, z = gl[i]
        x2, y2, z2 = gl[i + 1]
        if i not in mm:
            if z2 == z:
                hh += 2
            else:
                hh += 1

    return hh



with open(os.path.expanduser("~/PycharmProjects/gcj/2017/1C/B.in")) as f:
    m = int(f.readline().strip('\n'))
    # print m
    for i in range(m):
        ac,aj = [int(x) for x in f.readline().strip().split()]
        lc = []
        for j in xrange(ac):
            c,d = [int(x) for x in f.readline().strip().split()]
            lc.append((c,d))
        lj = []
        for j in xrange(aj):
            c, d = [int(x) for x in f.readline().strip().split()]
            lj.append((c, d))
        res = solve(ac, aj, sorted(lc), sorted(lj))
        # res2 = solve2(ac, aj, sorted(lc), sorted(lj))
        # if res != res2:
        #     print 'AAAA: ' + str(res) + '  ' + str(res2)
        print 'Case #' + str(i+1) + ': ' + str(res)