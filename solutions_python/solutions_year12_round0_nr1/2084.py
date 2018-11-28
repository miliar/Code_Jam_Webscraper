
instr = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
y qee
z"""
outstr = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
a zoo
q"""

mapping = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'

for ind in range(0, len(instr)):
	c = instr[ind]
	if c not in mapping.keys():
		mapping[c] = outstr[ind]
	elif mapping[c] != outstr[ind]:
		print "woah, problem! ", c, outstr[ind]

def test():
	for c in alpha:
		if c not in mapping.keys():
			print "%s is not in." % c
	s = ([c for c in mapping.values() if c in alpha])
	s.sort()
	s = ''.join(s)
	print s
	for c in alpha:
		if c not in s:
			print "%s not encoded." % c

def convert(s):
	news = ''
	for c in s:
		news += mapping[c]
	return news

print mapping

test()

f = open('a-small.txt')
outstr = ''
outf = open('a-small.out', 'w')
num = int(f.readline())
for l in range(0,num):
	line = f.readline().strip()
	output = convert(line)

	outstr = "Case #%d: %s\n" % (l+1, output)

	# output
	print outstr,
	outf.write(outstr)

f.close()
outf.close()
