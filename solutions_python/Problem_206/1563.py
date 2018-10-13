for i in range(int(input())):
	d,n=[int(x) for x in input().split()]
	lt=-float('inf')
	for _ in range(n):
		k,s=[int(x) for x in input().split()]
		t=(d-k)/s
		if t>lt:
			lt=t
		#print(lt)
	#print(lt)
	ans=d/lt
	print('Case #{}: {}'.format(i+1,ans))