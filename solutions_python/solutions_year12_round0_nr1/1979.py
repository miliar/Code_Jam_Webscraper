din = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
y qee"""

dout = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
a zoo"""

din = din.replace(" ", "").replace("\n", "")
dout = dout.replace(" ", "").replace("\n", "")

missingin = [True for i in xrange(ord('a'), ord('z')+1)]
missingout = [True for i in xrange(ord('a'), ord('z')+1)]

mp = dict()
for i in xrange(len(din)):
	missingin[ord(din[i])-ord('a')] = False
	missingout[ord(dout[i])-ord('a')] = False
	mp[din[i]] = dout[i]
missingin = [chr(c) for c in xrange(ord('a'), ord('z')+1) if missingin[c-ord('a')]][0]
missingout = [chr(c) for c in xrange(ord('a'), ord('z')+1) if missingout[c-ord('a')]][0]
mp[missingin] = missingout
mp[" "] = " "
f = open("a.in", "r")
din = f.read()
f.close()

sout = ""
din = din.split("\n")[1:]
nline = 1
for line in din:
	if line == "": continue
	sout += "Case #%d: " % (nline)
	for c in line:
		sout += mp[c]
	sout += "\n"
	nline += 1

f = open("a.out", "w")
f.write(sout)
f.close()
print sout
