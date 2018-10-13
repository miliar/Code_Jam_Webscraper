for xyz in range(int(input())):
	d,n = map(int,input().split())
	a = []
	ans = 100000000000000000
	for i in range(n):
		a.append(list(map(int,input().split())))
		k = a[i][0]
		s = a[i][1]
		t = (d-k)/s 
		ans = min(ans,d/t)	
	# low = 1
	# high = 1000000000
	# pos = 1
	# while low <= high:
	# 	mid = (low+high)/2
	# 	valid = True
	# 	for i in a:
	# 		k = i[0] # start pos
	# 		s = i[1] # speed
	# 		if s >= mid:
	# 			continue
	# 		x = mid*(k/(mid-s))
	# 		if x < d:
	# 			valid = False
	# 			break
	# 	if valid:
	# 		pos = mid
	# 		low = mid+0.0000001
	# 	else:
	# 		high = mid-0.0000001
	print("Case #"+str(xyz+1)+': ',end='')		
	print(ans)					
				
