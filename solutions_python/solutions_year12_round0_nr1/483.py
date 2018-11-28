src = """ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"""
dst = """our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"""
#d = dict(zip(src, dst))
#d['q'] = 'z'
#d['z'] = 'q'

from string import maketrans, translate
trans = maketrans(src+'zq', dst+'qz')

fin = open("A.in")
fout = open("A.out", 'w')

n = int(fin.readline())
for i in range(n):
	s = translate(fin.readline(), trans)
	fout.write("Case #%d: %s"%(i + 1, s))
fout.close()
	