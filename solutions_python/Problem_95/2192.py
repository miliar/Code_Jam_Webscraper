
P = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'.replace(' ','')
Q = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'.replace(' ','')
G1=[' ']
S1=[' ']
limit = len(P)
 
for i in range(limit):
	if (P[i]) not in G1:
		G1.append(P[i])
		S1.append(Q[i])
G1.append('q')
S1.append('z')
G1.append('z')
S1.append('q')

fin = open("A-small.IN", "r")
fout = open("outA1.out", "w")
n = int(fin.readline())

for i in range(n):
	g = fin.readline()
	g = g.strip('\n')
	lim = len(g)
	fout.write('Case #'+str(i+1)+': ')
	for j in range(lim):
		fout.write( S1[G1.index(g[j])] )
	fout.write('\n')

fin.close()
fout.close()
	
		