import sys
from string import maketrans

if len(sys.argv) < 2:
	print "No file name supplied."
	sys.exit(2)

known = {"y":"a","e":"o","q":"z"}

phrases = [
			("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi"),
			("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"),
			("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv")
]

english_pool = list("bcdefghijklmnpqrstuvwxy")
googler_pool = list("abcdfghijklmnoprstuvwxz")

for phrase in phrases:
	for i in range(len(phrase[0])):
		en, go = phrase[0][i], phrase[1][i]
		if go in known.keys():
			continue
		if en != ' ':
			known[go]=en
			del english_pool[english_pool.index(en)]
			del googler_pool[googler_pool.index(go)]
			
if len(english_pool) > 1:
	print "Could not determine full English -> Googlerese mapping"
	sys.exit(1)
elif len(english_pool) == 1:
	known[googler_pool[0]] = english_pool[0]

trans = maketrans("".join(known.keys()), "".join(known.values()))

fin = open(sys.argv[1], "r")
fout = open(sys.argv[1].rsplit(".",1)[0]+".out", "w")
count = int(fin.readline().rstrip())

for i in range(count):
	if i!=0:
		fout.write("\n")
	line = fin.readline().rstrip()
	fout.write("Case #%d: %s"%(i+1, line.translate(trans)))