x=int(input())
for a0 in range(x):
	a=int(input())
	n = list(str(a))
	i=len(n)
	if n == sorted(n):
		print('Case #'+str(a0+1)+": "+"".join(n))
	else:
		while 1==1:
			k=0
			while n[k]<=n[k+1]:
				k+=1
			n[k] =str(int(n[k])-1)
			n[k+1:]=['9']*(i-k-1)
			# print(n)
			if n==sorted(n):
				print('Case #'+str(a0+1)+": "+str(int("".join(n))))
				break		
