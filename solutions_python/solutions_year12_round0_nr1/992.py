
a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi' + \
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd' + \
'de kr kd eoya kw aej tysr re ujdr lkgc jv'

b = 'our language is impossible to understand' + \
'there are twenty six factorial possibilities' + \
'so it is okay if you want to just give up'

d = {}
for i in xrange(len(a)):
	d[a[i]] = b[i]

#print sorted(d.keys())
#print sorted(d.values())
d['q'] = 'z'
d['z'] = 'q'

T = int(raw_input())
for idx in xrange(1, T + 1):
	s = raw_input()
	t = []
	for x in s: t.append(d[x])
	print 'Case #%d: %s' % (idx, ''.join(t))
