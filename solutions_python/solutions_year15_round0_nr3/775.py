f=open('C-small-attempt0.in','r')
out=open('C0.txt','w')
def sign(x):
	if x<0:
		return -1
	elif x>0:
		return 1
	else:
		return 0
multtable=	[[1,2,3,4],
			 [2,-1,4,-3],
			 [3,-4,-1,2],
			 [4,3,-2,-1]]
n= int(f.readline())
for i in range(1, n+1):
	flag1=False
	flag2=False
	flag3=False
	s1=1
	s2=1
	s3=1
	temp=f.readline().split()
	x=int(temp[1])
	stng=f.readline()[:-1]*x
	stng=stng.replace('i','2')
	stng=stng.replace('j','3')
	stng=stng.replace('k','4')
	for m in (stng):
		if not flag1:
			s1=sign(s1)*multtable[abs(s1)-1][int(m)-1]
			if s1==2:
				flag1=True
		elif not flag2:
			s2=sign(s2)*multtable[abs(s2)-1][int(m)-1]
			if s2==3:
				flag2=True
		else:
			s3=sign(s3)*multtable[abs(s3)-1][int(m)-1]
	if s3==4:
		flag3=True
	print(flag1,flag2,flag3)
	print(s3)
	if flag3:
		out.write("Case #"+str(i)+": "+"YES"+"\n")
	else:
		out.write("Case #"+str(i)+": "+"NO"+"\n")
out.close()
