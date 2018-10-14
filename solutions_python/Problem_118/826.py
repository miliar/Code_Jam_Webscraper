from math import sqrt
def ss(aint):
	a=str(aint)
	for i in range(len(a)/2):
		if a[i]!=a[-i-1]:
			return 0;
	return 1;



n=int(sqrt(1e14)+1)
ff=[0]*n
ff[1]=1
for gg in xrange(2,n):
	if ss(gg):
		if ss(gg**2):
			ff[gg]=ff[gg-1]+1
		else:
			ff[gg]=ff[gg-1]
	else:
		ff[gg]=ff[gg-1]



def geshu(A,B):
	sa=(int(sqrt(A)))
	saa=(int(sqrt(A))-1)
	sb=(int(sqrt(B)))
	if sa**2==A:
		return ff[sb]-ff[saa]
	else:
		return ff[sb]-ff[sa]


fp=open('C-large-1.in','r')
ll=fp.readline()
ll=ll[0:-1]
fout=open('out.txt','w')
for i in range(int(ll)):
	kk=fp.readline()
	kk=kk[0:-1]
	tt=kk.split(" ")
	n=int(tt[0])
	m=int(tt[1])
#	print b
#	print "\n"
	fout.write("Case #%d: %d\n"%(i+1,geshu(n,m)))


fp.close()
fout.close()


