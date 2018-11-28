import string

fileName = 'A-small-attempt0.in'

f = open(fileName, 'r')
lines = map(lambda s: s.strip(), f.readlines())
count = int(lines[0])

str1 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
str2 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

mapping = {'q': 'z', 'z': 'q'}
for counter, _ in enumerate(str2):
	mapping[str2[counter]] = str1[counter]


for counter, line in enumerate(lines[1:]):
	print 'Case #%i: ' % (counter + 1),
	s = ''
	for c in line:
		s += mapping[c]
	print s
