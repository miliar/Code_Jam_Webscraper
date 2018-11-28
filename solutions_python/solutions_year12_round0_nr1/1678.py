import string, sys

orig = '''y qee
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''
trans ='''a zoo
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

m = {}

def translate(s):
	return string.join(map(m.get, s), '')

for i in xrange(len(orig)):
	m[orig[i]] = trans[i]

m['z'] = 'q'

assert translate(orig) == trans

n = int(sys.stdin.readline())
i = 1
for line in sys.stdin:
	sys.stdout.write('Case #%d: %s' % (i, translate(line)))
	i+=1
