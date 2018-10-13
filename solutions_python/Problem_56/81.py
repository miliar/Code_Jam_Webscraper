#!/usr/bin/env python
p = 'A'
s = 'small-attempt%d' % 0
l = 'large'
current = '%s-%s' % (p, l)

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def test(a, i, j, n, k, t):
    ret = [True for e in xrange(5)]
    for l in xrange(k):
        if ret[1]:
            if i < k - 1:
                ret[0] = False
                ret[1] = False
            if j > n - k:
                ret[1] = False
                ret[2] = False
                ret[3] = False
            if a[i - l][j + l] != t:
                ret[1] = False
        if ret[0]:
            if a[i - l][j] != t:
                ret[0] = False
        if ret[2]:
            if a[i][j + l] != t:
                ret[2] = False
        if ret[4]:
            if i > n - k:
                ret[3] = False
                ret[4] = False
            if a[i + l][j] != t:
                ret[4] = False
        if ret[3]:
            if a[i + l][j + l] != t:
                ret[3] = False
    #print "\n".join("".join(k) for k in a), i, j, t, ret
    ret = True in ret
    return ret

def inrow(a, n, k):
    s = n - k
    b = False
    r = False
    for i in xrange(n):
        for j in xrange(n):
            #print i,j
            if b and r:
                break
            if a[i][j] == "B":
                if not b:
                    b = test(a, i, j, n, k, "B")
            elif a[i][j] == "R":
                if not r:
                    r = test(a, i, j, n, k, "R")
    if b and r:
        return "Both"
    elif b and not r:
        return "Blue"
    elif not b and r:
        return "Red"
    else:
        return "Neither"

t = int(lines[0])

line = 1
for i in xrange(1, t + 1):
    s = lines[line].split()
    n, k = map(int, s)
    line += 1
    a = []
    for j in xrange(n):
        row = list(lines[line + j])
        if len(row) > n:
            row.pop()
        a.append(row)
    line += n
    for l in a:
        for m in xrange(n):
            if l[m] == ".":
                l.pop(m)
                l.insert(0, ".")
    print "Case #%d: %s" % (i, inrow(a, n, k))
    g.write("Case #%d: %s\n" % (i, inrow(a, n, k)))

g.close()
