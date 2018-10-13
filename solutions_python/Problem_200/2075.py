k,i=17,0
digits,num,fin=[1,2,3,4,5,6,7,8,9],[[1,2,3,4,5,6,7,8,9]],[]
fin.extend(num[-1])
while i<k:
	temp=[]
	for m in digits:
		for n in num[0]:
			if m<=int(str(n)[0]):temp.append(int(str(m)+str(n)))
	num[-1]=temp
	fin.extend(temp)
	i+=1
num=sorted(set(fin))
f=open("B-large.in")
for _ in xrange(int(f.readline().strip())):
	n=int(f.readline().strip())
	for x in num:
		if x<=n:result=x
		else:break
	print "Case #%d: %d"%(_+1,result)	