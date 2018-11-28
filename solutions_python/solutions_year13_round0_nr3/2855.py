cycle = raw_input()
cycle = int(cycle)

for i in range(cycle):
	result = 0
	a,b = raw_input().split()
	ia = int(a);
	ib = int(b);
	j=0
	while j**2<ia:
		j+=1
	while j**2<=ib:
		if str(j)==(str(j)[::-1]):
			if str(j**2)==(str(j**2)[::-1]):
				result+=1
				
		j+=1
	print 'Case #'+str(i+1)+': '+str(result)