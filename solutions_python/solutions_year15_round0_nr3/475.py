te = "1ijk"
td = "1ijki1kjjk1ikji1"
ts = "0000010101100011"
tb = {}
for i in xrange(16):
    tb[ord(te[i >> 2]), ord(te[i & 3])] = ord(td[i]) | (int(ts[i]) << 7)

def tt(x, y):
    return tb[x & 0x7f, y & 0x7f] ^ (x & 0x80) ^ (y & 0x80)

def pp(x, p):
    if p:
        t = pp(x, p >> 1)
        if p & 1:
            return tt(t, tt(t, x))
        else:
            return tt(t, t)
    else:
        return ord("1")

for tc in xrange(int(raw_input())):
    n, x = tuple(raw_input().split())
    n, x = int(n), int(x)
    s = raw_input()
    i = 0
    t0 = i

    l = set()
    e = ord("1")
    while i < n * x and (i % n, e) not in l:
        l.add((i % n, e))
        e = tt(e, ord(s[i % n]))
        i += 1
        if e == ord("i"):
            break
    else:
        print "Case #%d: NO" % (tc + 1)
        continue
#    t1 = i
#    print "i: " + (s * x)[t0:t1]

    l = set()
    e = ord("1")
    while i < n * x and (i % n, e) not in l:
        l.add((i % n, e))
        e = tt(e, ord(s[i % n]))
        i += 1
        if e == ord("j"):
            break
    else:
        print "Case #%d: NO" % (tc + 1)
        continue
#    t2 = i
#    print "j: " + (s * x)[t1:t2]

    l = set()
    e = ord("1")
    while i < n * x and (i % n, e) not in l:
        l.add((i % n, e))
        e = tt(e, ord(s[i % n]))
        i += 1
        if e == ord("k"):
            break
    else:
        print "Case #%d: NO" % (tc + 1)
        continue
#    t3 = i
#    print "k: " + (s * x)[t2:t3]

    e = ord("1")
    while i % n:
        e = tt(e, ord(s[i % n]))
        i += 1
    c = ord("1")
    for j in s:
        c = tt(c, ord(j))
    if tt(e, pp(c, x - (i / n))) == ord("1"):
        print "Case #%d: YES" % (tc + 1)
    else:
        print "Case #%d: NO" % (tc + 1)
