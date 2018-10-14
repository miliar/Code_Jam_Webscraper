import sys

ss = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
ps = ["our language is impossible to understand","there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

d = {}
d['q'] = 'z'
d['z'] = 'q'
for s, p in zip(ss, ps):
	for sc, pc in zip(s, p):
		if sc not in d:
			d[sc] = pc
		assert d[sc] == pc

k = int(sys.stdin.readline())
s = 10
for id, line in enumerate(sys.stdin):
	line = line.strip()
	line = ''.join(map(lambda x: d[x], line))
	print 'Case #%d: %s' % (id+1, line)

# print ''.join(sorted(d.keys()))
# print ''.join(sorted(d.values()))
# print d