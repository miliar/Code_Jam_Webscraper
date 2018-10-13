import sys


fp = open(sys.argv[1])
N = int(fp.readline().strip())

def valid(v, rs, re, cs, ce):
    #print "valid", v, rs, re, cs, ce
    s = {}
    for r in range(rs, re + 1):
        for c in range(cs, ce + 1):
            s[v[r][c]] = True
            if len(s) > 2:
                return None
            if len(s) == 2 and '?' not in s:
                return None
    if '?' in s:
        s.pop('?')
    if len(s.keys()) == 0:
        return None

    #print "valid"
    return s.keys()[0]

def bar(v, rs, re, cs, ce):
    #print "bar", rs, re, cs, ce
    if rs >= re or cs >= ce or rs  >= len(v) or cs >= len(v[0]):
        return
    found = None
    rstop = re - 1
    cstop = ce - 1
    for r in range(re - 1, rs -1, -1):
        if found:
            break
        for c in range(ce - 1, cs - 1, -1):
            found = valid(v, rs, r, cs, c)
            if found:
                rstop = r
                cstop = c
                break
    #print rstop, cstop, found
    for r in range(rs, rstop + 1):
        for c in range(cs, cstop + 1):
            v[r][c] = found
    #bar(v, rstop + 1, re, cs, cstop + 1)
    bar(v, rstop + 1, re, cs, ce)
    bar(v, rs, rstop + 1, cstop + 1, ce)

def foo():
    R, C = fp.readline().strip().split(" ")
    R = int(R)
    C = int(C)
    v = []
    for i in range(R):
        v.append(list(fp.readline().strip()))
    bar(v, 0, R, 0, C)
    for vv in v:
        print ''.join(vv)

for case in range(N):
    print "Case #%d:" % (case + 1)
    foo()

fp.close()
