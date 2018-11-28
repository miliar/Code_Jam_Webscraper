n=int(input())

for nb in range(n) : 
	
	n,p=[int(e) for e in input().split()]

	d={n:1}

	while p>0:
		#print(i)
		#print(d)
		m=max(d.keys())
		v= d[m]
		p-=v
		del(d[m])
		if m//2 in d :
			d[m//2]+=v
		else :
			d[m//2]=v
		if (m-1)//2 in d:
			d[(m-1)//2]+=v
		else :
			d[(m-1)//2]=v

	print("Case #"+str(nb+1)+":",m//2,(m-1)//2)

