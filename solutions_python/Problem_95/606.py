import sys,os

def dbg(msg, *args):
	print >>sys.stderr,msg%args

def getline():
	return sys.stdin.readline().rstrip()

def gen():
	charmap = { "q":"z","e":"o","y":"a" }
	googlerese = """\
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""
	english = """\
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""
	r  = range(ord('a'),ord('z')+1)
	for i in range(len(googlerese)):
		g,e = googlerese[i], english[i]
		if ord(g) in r:
			if g in charmap:
				if not charmap[g] == e: print "ERROR %s = %s (should be %s)" % (g,e,charmap[g])
			else:
				charmap[g] = e

	g_missing = []
	e_missing = []
	for ch in [ chr(x) for x in r ]:
		if not ch in charmap: g_missing.append(ch)
		if not ch in charmap.values(): e_missing.append(ch)

	#print "Missing googlerese chars %s" % g_missing
	#print "Missing english chars %s" % e_missing
	if len(g_missing) == len(e_missing) == 1:
		charmap[g_missing[0]] = e_missing[0]
	return charmap

charmap = gen()
#dbg("CHARMAP %s %d -> %d", repr(charmap), len(set(charmap.keys())), len(set(charmap.values())))

T = int(getline())
for case in range(1,T+1):
	l = getline()
	sys.stdout.write("Case #%d: " % case)
	for ch in l:
		if ch == ' ': sys.stdout.write(ch)
		else: sys.stdout.write(charmap[ch])
	print