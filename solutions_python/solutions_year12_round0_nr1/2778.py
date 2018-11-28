G = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qgz"
E = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zvq"

d = {}

for i in range(len(G)):
	d[G[i]] = E[i]

fi = open('/home/rae/Desktop/inputG.in','r')
fo = open('/home/rae/Desktop/outputG.out','w')

cases = int(fi.readline())

for c in range(0,cases):
	line = fi.readline().strip()
	fo.write("Case #"+str(c+1)+": ")
	for e in line:
		fo.write(d[e])
	if (c+1)<cases: 
		fo.write("\n")
	
