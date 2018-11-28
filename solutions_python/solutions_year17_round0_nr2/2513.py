def t(n):
	for i in range(len(n)-1):
		if int(n[i])>int(n[i+1]):
			return 0
	return 1

def tidy(n):
	if t(n):
		return n
	l=len(n)
	a=list(n)
	if l<2:
		return n
	for i in range(l-1):
		if int(a[i])>int(a[i+1]):
			a[i]=str(int(a[i])-1)
			break
	else:
		return n
	return tidy(''.join(a[:i+1]+['9']*(l-i-1)))

for i in range(int(input())):
	n=str(input())
	ans=int(tidy(n))
	print('Case #%d: %d'%(i+1,ans))