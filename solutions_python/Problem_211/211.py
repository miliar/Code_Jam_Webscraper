for xyz in range(1,int(input())+1):
	print("Case #"+str(xyz)+': ',end='')
	n,k = map(int,input().split())
	u = float(input())
	a = list(map(float,input().split()))
	if n == k:
		a.sort()
		a.append(1)
		n += 1
		pos = 1
		# print(a)
		while u > 0 and pos < n:
			if pos*(a[pos]-a[pos-1]) < u:
				u -= pos*(a[pos]-a[pos-1])
				for i in range(pos):
					a[i] = a[pos]
			else:
				for i in range(pos):
					a[i] = a[pos-1]+(u/pos)
				u = 0
			pos += 1
			# print(a)
		ans = 1
		for i in a:
			ans *= i	
		print(round(ans,8))				