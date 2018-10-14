z=[]
def flip(d,j,k):
	return d[:j] + ''.join(['-' if i=='+' else '+' for i in d[j:j+k]]) + d[j+k:]
for kjlfksjdaf in range(int(input())):
	st, k = input().split()
	k = int(k)
	c = 0
	n = len(st)
	flag = 0
	for i in range(2**(n-k+1)):
		d = st
		stri = format(c, "#0" + str(n-k+3) + "b")[2:]
		for j,v in enumerate(stri):
			if v=='1':
				d = flip(d,j,k)
		if set(d)==set('+'):
			flag = 1
			z.append(sum(map(int, stri)))
		c+=1
	if flag==0:
		z.append("IMPOSSIBLE")
for c,i in enumerate(z): print("Case #" + str(c+1) + ":", i)