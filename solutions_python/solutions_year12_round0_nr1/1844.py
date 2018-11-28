import sys
al = ['q', 'z']
tr = ['q', 'z']
key = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

lines = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv']
al = [a for a in 'abcdefghijklmnopqrstuvwxyz']
tr = [a for a in 'abcdefghijklmnopqrstuvwxyz']
key = {}
sample = ['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up']

lines = " ".join(lines).split()
sample = " ".join(sample).split()
for cip, pt in zip(lines,sample):
	for i in range(len(cip)):
		c,p = cip[i],pt[i]
		key[c] = p
		if c in tr:
			tr.remove(c)
			al.remove(p)

lines = []
fname = sys.argv[1]
fp = open(fname)
num = int(fp.next())
for i in range(num):
	lines.append(fp.next().strip())
fp.close()
# just because. This question is obviously just for fun
key[' '], key['q'], key['z'] = ' ', 'z','q'
for line, index in zip(lines, range(1,num+1)):
	nl = []
	for letter in line:
		if letter in key:
			nl.append(key[letter])
		else: nl.append(letter)
	nl = ''.join(nl)
	print "Case #%s:" % index, nl
