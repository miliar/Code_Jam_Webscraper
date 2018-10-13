timer=0
lines=[]
file = open('A-large.in','r')
allLines = file.readlines()
file.close()
for line in allLines:
	a = line.split()
	lines.append(a)

N=int(lines[0][0])
def sgn(i):
	if i>0:
		return 1
	if i<0:
		return -1
	else:
		return 0

def move(X,Y,i,j):
	global bn,timer,o,b
	#print 'before', X,Y,i,j
	while X<>i:
		X+=sgn(i-X)
		Y+=sgn(j-Y)
		timer+=1
		#print 'AT TIME',timer, X,Y,i,j
	Y+=sgn(j-Y)
	if X>0:
		o=X;b=Y
	else:	
		b=X;o=Y
	timer+=1
	#print 'after',X,Y,i,j	

for count in range(N):
	timer=0
	#print lines[2]
	seq=lines[count+1]
	#print seq
	bn=int(seq[0])
	dic={}

	for i in range(1,len(seq),2):
		#print 'i,seq[i]',i,seq[i]
		if seq[i]=='O':
			X='O'
			i1=int(seq[i+1])
			dic[(i+1)/2]=[1,i1]
		else:
			X='B'
			i1=int(seq[i+1])
			dic[(i+1)/2]=[-1,-i1]
	l=1;o=1;b=-1
	#print 'dic,l',dic,l
	while l<=bn:
		#print 'O and B',o,b
		if dic[l][0]>0:	
			X=o;i=dic[l][1];Y=b
		else:
			X=b;i=dic[l][1];Y=o
		k=l
		#print 'X , k was with dic', X,k,dic[k][0]		

		while k<=bn and dic[k][0]==sgn(X):
			k+=1
		#print 'should be at k',k
		if not k>bn:
			if dic[k][0]>0:
				Y=o;j=dic[k][1]
			else:
				Y=b;j=dic[k][1]
		else:
			Y=-dic[k-1][0];j=-dic[k-1][1]
			
		move(X,Y,i,j)

		l+=1
	print 'Case #%d: %d' % (count+1,timer)
		#print 'l,bn,timer,O,B',l,bn,timer,o,b

