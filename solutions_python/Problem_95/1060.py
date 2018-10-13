import sys

texts_en = [
	'our language is impossible to understand',
	'there are twenty six factorial possibilities',
	'so it is okay if you want to just give up'
]

texts_go = [
	'ejp mysljylc kd kxveddknmc re jsicpdrysi',
	'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
	'de kr kd eoya kw aej tysr re ujdr lkgc jv'
]

def analyze():
	translator = {}
	for i in xrange(3):
		for c in xrange(len(texts_en[i])):
			if texts_go[i][c] in 'abcdefghijklmnopqrstuvwxyz':
				translator[texts_go[i][c]] = texts_en[i][c]
	translator['q'] = 'z'
	translator['z'] = 'q'
	return translator

total = -1
count = 1

tr = analyze()

for line in sys.stdin:
	if total < 0:
		total = int(line)
		continue
	sys.stdout.write('Case #%d: ' % (count))
	for c in line:
		if c in tr: sys.stdout.write(tr[c])
		else: sys.stdout.write(c)
	count += 1