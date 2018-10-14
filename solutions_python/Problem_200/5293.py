n1=int(input())
p1=list()
for i in range(n1):
	l=int(input())
	p1.append(l)
for i in range(0,len(p1)):
	for j in range(p1[i],0,-1):
		dig=list()
		n1=j
		while(n1!=0):
			d=int(n1%10)
			dig.append(d)
			n1=int(n1/10)
		dig.sort()
		num2 = int(''.join(map(str,dig)))
		if(num2==j):
			print("Case #{}: {}".format(i+1,num2))
			break
