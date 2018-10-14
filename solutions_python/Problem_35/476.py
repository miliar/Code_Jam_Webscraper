fin = open('basin.in','r')
fout = open('basin.out','w')

T=0
T=int(fin.readline())

def sink(j,i,wflow):
	s=[]
	while (True):
		fdir=wflow[j][i]
		#print j,i,fdir
		if (fdir!=-1):
			if (fdir==0):
				j=j-1
			elif (fdir==1):
				i=i-1
			elif (fdir==2):
				i=i+1
			elif (fdir==3):
				j=j+1
			#print "sink ",i,j
		else:
			s.append(j)
			s.append(i)
			break	
	return s

for k in range(T):
	fout.write("Case #"+str(k+1)+":\n")
	buf = fin.readline().split()
	H = int(buf[0])
	W = int(buf[1])
	amap=[]
	for j in range(H):
		buf = fin.readline().split()
		amap.append([])
		for i in range(W):
			amap[j].append(int(buf[i]))
		
	flow=[]
	for j in range(H):
		flow.append([])
		for i in range (W):
			alts=[]	
			if (j-1<0):
				alts.append(10001)
			else:
				alts.append(amap[j-1][i])
			if (i-1<0):
				alts.append(10001)
			else:
				alts.append(amap[j][i-1])
			if (i+1>=W):
				alts.append(10001)
			else:
				alts.append(amap[j][i+1])
			if (j+1>=H):
				alts.append(10001)
			else:
				alts.append(amap[j+1][i])
			
			hmax = amap[j][i]
			fdir=-1;
			for k in range(4):
				if (alts[k]<hmax):
					#print "test ",i,j,alts[k],hmax,k
					hmax=alts[k]
					fdir=k;
			flow[j].append(fdir)
			#print i,j,amap[j][i],fdir
	#print flow
	bsink=[]
	for j in range(H):
		bsink.append([])
		for i in range (W):
			s = sink(j,i,flow);
			bsink[j].append(s)
	sinks=[]
	for j in range(H):
		for i in range (W):
			if (not bsink[j][i] in sinks):
				sinks.append(bsink[j][i])
	#print sinks
	letters=[]
	char = 'a'
	for l in range(len(sinks)):
		letters.append(char)
		char=chr(ord(char)+1)
	#print letters
	
	for j in range(H):
		for i in range (W):
			label = sinks.index(bsink[j][i])
			out = letters[label]
			fout.write(out)
			if (i<W-1):
				fout.write(" ")
		fout.write("\n")
