import os

def is_empty(row):
    for x in row:
        if x != '?': return False
    return True

def fill(row,c):
    res = ''
    b = True
    g = ' '
    cc = 0
    for i in xrange(c):
        if row[i] == '?':
            if b:
                cc += 1
            else:
                res += g
        else:
            g = row[i]
            res += g
            b = False
    if cc > 0:
        res = res[0]*cc + res
    return res



def solve(r,c,m):
    mm = []

    b = True
    gg = ''
    cc = 0
    for i in xrange(r):
        row = m[i]
        if is_empty(row):
            if b:
                cc += 1
            else:
                mm.append(gg)
        else:
            gg = fill(row,c)
            mm.append(gg)
            b = False

    if cc > 0:
        mm = [mm[0]]*cc + list(mm)

    return mm

with open(os.path.expanduser("~/PycharmProjects/gcj/2017/1A/A.in")) as f:
    m = int(f.readline().strip('\n'))
    print m
    for i in range(m):
        r,c = [int(x) for x in f.readline().strip().split(' ')]
        m = []
        for j in xrange(r):
            row = f.readline().strip()
            m.append(row)
        res = solve(r,c,m)
        print 'Case #' + str(i+1) + ': '
        for x in res:
            print x