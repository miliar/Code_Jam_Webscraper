n2=int(input())
p2=list()
for i in range(n2):
	l=int(input())
	p2.append(l)
for i in range(0,len(p2)):
	for j in range(p2[i],0,-1):
		dig=list()
		n3=j
		while(n3!=0):
			d=int(n3%10)
			dig.append(d)
			n3=int(n3/10)
		dig.sort()
		num2 = int(''.join(map(str,dig)))
		if(num2==j):
			print("Case #{}: {}".format(i+1,num2))
			break
