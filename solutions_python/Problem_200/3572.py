def tidy(n):
	n=str(n)
	for i in range(len(n)-1):
		if int(n[i])>int(n[i+1]): return False
	return True

t=int(input())
for cn in range(1,t+1):
	n=int(input())
	while not tidy(n): n-=1
	print("Case #{}: {}".format(cn,n))
