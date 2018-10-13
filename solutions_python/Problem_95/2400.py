mapa = {'q': 'z', 'z': 'q'}

def crear_mapeo(sg, se):
	for i in range(len(sg)):
		mapa[sg[i]] = se[i]

def traducir(s):
	english = ""
	for c in s:
		english += mapa[c]
	return english
	
s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

crear_mapeo(s1, "our language is impossible to understand")
crear_mapeo(s2, "there are twenty six factorial possibilities")
crear_mapeo(s3, "so it is okay if you want to just give up")

n = int(raw_input())
for i in range(n):
	s = raw_input()
	print "Case #{}: {}".format(i+1, traducir(s))