def isare(n,s,s1):
	if s%3==0 and s1:
		if s/3>=n:
			return [1,0]
		if n<=s/3+1 and s/3-1>=0:

			return [1,1]
		else:
			return [0,0]
	if n<=s/3+s%3:
		if s%3==2 and n==s/3+s%3 and s1:
			return [1,1]
		if s%3==2 and n==s/3+s%3:
			return [0,0]
		return [1,0]
	else:
		return [0,0]

def tr(ss):
	n=int(ss.split()[0])
	s=int(ss.split()[1])
	p=int(ss.split()[2])
	res=0
	for i in range(n):
		tt=isare(p,int(ss.split()[3+i]),s)
		res+=tt[0]
		if tt[1]:
			s-=1
	return res

	

file = open('b.in','r')

t=int(file.readline())
ret=[]
for x in file.readlines():
	x=x.replace('\n','')
	x=x.replace('\r','')
	ret.append(tr(x))
file2=open('b.out','w')
for x in range(len(ret)):
	file2.write('Case #'+str(x+1)+': '+str(ret[x])+'\n')
file2.close()
file.close()

