import sys, string
f = sys.argv[1]

t = string.maketrans('ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz', 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq')

lines = open(f, 'r').readlines()
cases = int(lines[0])

for i, line in enumerate(lines):
	if i == 0: continue
	print 'Case #%i: %s' % (i, line.translate(t)),