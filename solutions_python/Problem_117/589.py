def ss(nn,mm,bb):
	cc=[]
	for ii in range(nn):
		for jj in range(mm):
			if(bb[ii][jj] not in cc):
				cc.append(b[ii][jj])
	cc.sort()
	cc.reverse()
	for ii in cc:
		hengsao=[1]*nn
		shusao=[1]*mm
		for jj in range(nn):
			if ii in bb[jj]:
				for kk in range(mm):
					if(bb[jj][kk]<0):
						hengsao[jj]=0
						break
		for jj in range(mm):
			if ii in ([bb[ww][jj] for ww in range(nn)]):
				for kk in range(nn):
					if(bb[kk][jj]<0):
						shusao[jj]=0
						break
		for jj in range(nn):
			for kk in range(mm):
				if(bb[jj][kk]==ii):
					if hengsao[jj]==1 or shusao[kk]==1:
						bb[jj][kk]=-1
					else:
						return "NO"		
	return "YES"


fp=open('B-large.in','r')
ll=fp.readline()
ll=ll[0:-1]
fout=open('out.txt','w')
for i in range(int(ll)):
	kk=fp.readline()
	kk=kk[0:-1]
	tt=kk.split(" ")
	n=int(tt[0])
	m=int(tt[1])
	a=n*["1"]
	b=[[0]*m for u in range(n)]
	for j in range(n):
		a[j]=fp.readline()[0:-1]
	for j in range(n):
		ww=a[j].split(" ")
		for k in range(m):
			b[j][k]=int(ww[k])
#	print b
#	print "\n"
	fout.write("Case #%d: %s\n"%(i+1,ss(n,m,b)))


fp.close()
fout.close()


