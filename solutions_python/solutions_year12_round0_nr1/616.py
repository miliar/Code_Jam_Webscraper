msgs = []
msgs.append(('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'))
msgs.append(('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'))
msgs.append(('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up'))
msgs.append(('yeq', 'aoz'))
trans = {}
for msg in msgs:
	for g, e in zip(*msg):
		trans[g] = e
alph = map(chr, range(97, 123))
f = None
t = None
for a in alph:
	if a not in trans:
		f = a
	if a not in trans.values():
		t = a
trans[f] = t
for i in xrange(int(raw_input())):
	print 'Case #%d: %s' % (i + 1, ''.join(map(trans.__getitem__, raw_input().strip())))
