src = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
y qee
z"""

dst = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
a zoo
q"""

def translate(s):
	return ''.join(map(lambda c: dst[src.find(c)], s))

T = int(raw_input())
for X in xrange(T):
	G = raw_input()
	S = translate(G)
	print("Case #%d: %s" % (X + 1, S))
