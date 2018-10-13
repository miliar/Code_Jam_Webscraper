lines = open('1.in').read().split('\n')
n = int(lines[0])
lines = lines[1:]
#print n, lines

d = {' ':' ','q':'z', 'z': 'q'}
a = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
'our language is impossible to understand',
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
'there are twenty six factorial possibilities',
'de kr kd eoya kw aej tysr re ujdr lkgc jv',
'so it is okay if you want to just give up',]

for i in xrange(0,len(a),2):	
	for j in xrange(len(a[i])):
		if a[i][j]!=' ':
			k, v = a[i][j], a[i+1][j]
			d[k] = v

fout = open('1.out', 'w')
for t in xrange(n):
	fout.write("Case #"+ str(t+1)+": " + "".join([d[c] for c in lines[t]  ]) + "\n")
fout.close()
	