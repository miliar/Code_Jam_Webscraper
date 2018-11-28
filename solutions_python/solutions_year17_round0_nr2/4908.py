def valid(i):
	i=list(i)
	if sorted(i)==i:
		return True
	else:
		return False
t=int(input())
for tc in range(t):
	n=int(input())
	print('Case #%d:'%(tc+1),end=' ')
	for i in range(n,0,-1):
		if(valid(str(i))):
			print(i)
			break
	
