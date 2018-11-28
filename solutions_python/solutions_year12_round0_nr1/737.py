ll = open('/Users/pittaya/Downloads/A-small-attempt0.in').readlines()
numcase = ll[0]

a = 'abcdefghijklmnopqrstuvwxyz'
b = 'ynficwlbkuomxsevzpdrjgthaq'
i = 1
for lll in ll[1:]:
	l = []
	for c in lll.strip():
		if (c != ' '):
			l.append(a[b.find(c)])
		else:
			l.append(' ')
	
	print 'Case #%d: %s' % (i, ''.join(l))
	i += 1