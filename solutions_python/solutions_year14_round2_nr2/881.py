#from scipy.misc import comb

R=[]

with open(r'B-small-attempt0.txt','rt') as arch:
	for line in arch:
		R.append([int(i) for i in line[0:-1].split()])
tt=R.pop(0)
def guin(o,n,c):
	win=0
	for i in range(o):
		for j in range(n):
			#print i,j,i&j,c
			if i&j<c:
				win+=1
	return win
t=0

while len(R)>0:
	t+=1
	linea=R.pop(0)
	old=linea[0]
	new=linea[1]
	catalina=linea[2]
	p=guin(old,new,catalina)

	print 'Case #%i: %i' %(t,p)


