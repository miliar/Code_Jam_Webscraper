fin = open("A-small.IN", "r")
fout = open("outA2.out", "w")
n = int(fin.readline())

for i in range(n):
	g = fin.readline()
	g = g.strip('\n')
	A,B = g.split(' ')
	#A,B = int(A),int(B)
	nDig = len(A)
	ctr = 0
	
	for j in range(int(A),int(B)):
		s = str(j)
		li=[]
		for x in range(nDig):
			li.append(s)
			s += s[0]
			s =  '' + s[1:]
			
		for y in li:
			if ((int(li[0]) < int(y)) and (int(y) <= int(B))):
				ctr += 1
		#fout.write( S1[G1.index(g[j])] )
	fout.write('Case #'+str(i+1)+': '+str(ctr)+'\n')

fin.close()
fout.close()