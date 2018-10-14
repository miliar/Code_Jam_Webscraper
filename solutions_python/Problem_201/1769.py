def maxMin(q):
	m1 = min(q)
	m2 = max(q)
	return [m2, m1]

def mod(q, w, x):
	n = int(q+w/2)
	x = x[:n] + '1' + x[n+1:]
	Rs = x.find('1', n+1) - (n+1)
	Ls = x[::-1].find('1', len(x)-n) - (len(x)-n)
	return [x, Ls, Rs]

def execute():
	[n, k] = input().split()
	n = int(n)
	k = int(k)
	x = ''
	while len(x)<n:
		x += '0'
	x = '1' + x + '1'
	while k>0:
		k-=1
		max0s = []
		for i in range(len(x)):
			max0s.append(x.find('1', i) - i)
		#print(max0s)
		m = max0s.index(max(max0s))
		#print(str(m) + ' ' + str(max0s[m]) + ' ' + str(x))
		[x, Ls, Rs] = mod(m, max0s[m], x)
		#print(x)
	#print(x)
	[Ls, Rs] = maxMin([Ls, Rs])
	return (str(Ls) + ' ' + str(Rs))
	#return ('Ls: '+ str(Ls) + ' ' + 'Rs: '+ str(Rs))


t = input()
t = int(t)
i = 1
while t>0:
	ans = execute()
	print("Case #" + str(i) + ": " + str(ans))
	t -= 1
	i +=1