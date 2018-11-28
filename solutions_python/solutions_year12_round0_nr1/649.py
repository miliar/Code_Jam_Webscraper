import sys

map = "yhesocvxduiglbkrztnwjpfmaq"

count = int(sys.stdin.readline())
for i in xrange(0, count):
	tc = i+1
	strin = sys.stdin.readline()[:-1]
	res = []
	for c in strin:
		if c <> ' ':
			res.append(map[ord(c)-ord('a')])
		else:
			res.append(c)

	print "Case #%d: %s" % ( tc, "".join(res) )