import sys

cypher = """y qee
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
plain = """a zoo
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

map = {}
for i in xrange(len(cypher)):
	map[cypher[i]] = plain[i]
map['z'] = 'q'

f = open(sys.argv[1], 'r')
i = 0
for line in f:
	print "Case #%d: "%i,
	i += 1
	
	for c in line:
		if c in map:
			sys.stdout.write(map[c])
		else:
			sys.stdout.write(c)