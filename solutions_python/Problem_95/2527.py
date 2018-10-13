from string import maketrans
s1 = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

s2 = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

d = dict(zip(s1, s2))
t1 = ""
t2 = ""
for k, v in d.iteritems():
    t1 += k
    t2 += v
t1 += 'z'
t2 += 'q'
t1 += 'q'
t2 += 'z'
table = maketrans(t1, t2)

n = int(raw_input())
for c in xrange(1, n + 1):
    line = raw_input()[:100]
    line = "Case #%d: %s" % (c, line.translate(table))
    print line.strip()
