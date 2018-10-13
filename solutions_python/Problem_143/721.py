t = input()
for x in range(t):
	a,b,k = map(int,raw_input().split())
	count=0
	for num in range(a):
		for num2 in range(b):
			j = num & num2
			if j<k:
				count+=1
	
	print "Case #"+str(x+1)+": "+str(count)
	
	
		