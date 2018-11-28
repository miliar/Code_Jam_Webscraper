def flip(k, x):
	for i in range(x):
		if k[i] == '+':
			k = k[:i] + '-' + k[i+1:]
		else:
			k = k[:i] + '+' + k[i+1:]
	return k

def execute():
	[k, n] = input().split()
	n = int(n)
	x = len(k)
	count = 0
	while True:
		k = k.lstrip('+')
		if(len(k)==0):
			break
		elif(len(k) < n):
			return 'IMPOSSIBLE'
		k = flip(k, n)
		count+=1
		'''
		q = k.find('+')
		if(q==-1):
			q = len(k)
		count += 1
		if(q > n):
			k = flip(k, q)
		else:
			k = flip(k,n)
		'''
	return count

t = input()
t = int(t)
i = 1
while t>0:
	ans = execute()
	print("Case #" + str(i) + ": " + str(ans))
	t -= 1
	i +=1