t = int(input())
for t0 in range(t):
	x = int(input())
	while x>0:
		n = list(str(x))
		n = [int(i) for i in n]
		#print(n)
		if all(n[i] <= n[i+1] for i in range(len(n)-1)):
			print('Case #{}: {}'.format(t0+1,x))
			break
		x-=1
	