T = int(input())
for t in range(1,T+1): 
	N, K = map(int,input().split())
	U = float(input())
	arr = list(map(float,input().split()))
	s = sum(arr)
	no = len(arr)
	opt = (s+U)/no
	above = 0
	remove = 0
	for a in arr:
		if a >= opt:
			above+=1
			remove+=a

	if above != no:
		add = (s+U-remove)/(no-above)
	else:
		add = arr[0]	
	answer = 1
	for a in arr:
		if a < opt:
			a = add
		answer*=a	
						
	print('Case #{}: {}'.format(t,answer))