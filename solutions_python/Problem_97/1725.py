def recycles(n):
	s=str(n)
	length=len(s)
	l=list(s)
	x=[]
	for i in range(0,length):
		newstr=''
		for j in l:
			newstr=newstr+j	
		l=l[-1:]+l[:-1]
		x.append(newstr)
	return x


#a=input('A')
#b=input('B')

#a=10
#b=40
#flist=[]
def calc_num_recycles(a,b):
	flist=[]
	t=0
	for n in range(a,b):
		x=recycles(n)
		
		#print x
		for ms in x:
			m=int(ms)
			if len(ms)!=len(str(m)):
				continue
			if len(str(n))!=len(str(m)):
				continue
			if n<m and a<=n and m<=b:
				flist.append((n,m))
				t=t+1
	flist=list(set(flist))
	return len(flist)




fp=open("C-small-attempt1.in")
n=fp.readline().strip()
i=1
while True:
	n=fp.readline().strip()
	if n=='':
		break
	l=n.split(' ')

	s1=l[0]
	s2=l[1]
	
	a=int(s1)
	b=int(s2)

	num_cycles=calc_num_recycles(a,b)
	print "Case #"+str(i)+":",num_cycles
	i=i+1

