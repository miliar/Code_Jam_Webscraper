import sys

g = {}
letters = 'abcdefghijklmnopqrstuvwxyz'
found = set()
for i, c in enumerate('ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'):
	g[c] = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'[i]
	found.add(c)
g['q'] = 'z'
g['z'] = 'q'
data = [x.strip() for x in open(sys.argv[1])]

T = int(data.pop(0))

for i, t in enumerate(data):
	s = []
	for c in t:
		s.append(g[c])
	print "Case #%d: %s" % ((i + 1), ''.join(s))
		