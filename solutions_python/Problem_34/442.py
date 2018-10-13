import re

#fin = open("A-small.in")
#fin = open("A-small-attempt0.in")
fin = open("A-large.in")
l, d, n = (int(i) for i in fin.readline().split())

wlist = []
plist = []

for i in xrange(d):
    wlist.append( fin.readline() )

for x in xrange(n):
    t = fin.readline()
    if t.endswith("\n"):
        t = t[:-1]
    t = t.replace("(", "[")
    t = t.replace(")", "]")
    plist.append( re.compile(t)  )

cnt = 1
for pat in plist:
    res = 0
    for w in wlist:
        if pat.match( w ):
            res += 1
    print "Case #%d: %d" % (cnt, res)
    cnt += 1

fin.close()
