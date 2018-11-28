import string

g = open("a.txt")
h = open("a.r.txt")
d = {}
_g = g.read()
_h = h.read()

for i in xrange(len(_g)):
    d[_g[i]] = _h[i]

for x in string.lowercase:
    try:
        print x, ' -> ', d[x]
    except:
        print 'No eq for ', x

g.close()
h.close()

i = open("A-small-attempt0.in")
t = int(i.readline())
r = ""
for _ in xrange(t):
    r += "Case #%d: " % (_+1)
    for c in i.readline():
        r += d[c]
print r
o = open("a-out.txt", "w")
o.write(r)
o.close()
i.close()