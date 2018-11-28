# -*-coding:utf8 -*
from parsing import TextGen
infile = "A-small.in"
outfile = "a.out"

########################

def algo(inp):
	smax = inp.int
	audience = inp.str
	if smax == 0: return 0
	friends = 0
	cmp = 0
	for (s,n) in enumerate(audience):
		n = int(n)
		cmp += n
		if cmp <= s:
			friends += 1
			cmp += 1
	return friends
		


########################

inp = TextGen(infile)
cases = inp.int
with open(outfile,'w') as outdata:
	for case in range(1, cases+1):
		outdata.write("Case #%d: %s\n" % (case, algo(inp)))
