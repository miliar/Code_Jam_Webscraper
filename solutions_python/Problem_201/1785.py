def fn(l):
	m = list(map(len,l))
	ind = m.index( max(m) )
	del m

	l1 = l[ind][:]
	del l[ind]

	i = len(l1)
	i = i//2 + i%2

	right = l1[:i-1]
	left = l1[i:]

	l.append(right)
	l.append(left)

	return (len(left),len(right))


	
T = int(input())
for loop in range(1,T+1):
	N,K = [ int(x) for x in input().split() ]
	l = []
	l.append([0]*N)
	ans = 0
	for i in range(K):
		ans = fn(l)
	print("Case #",loop,": ",max(ans)," ",min(ans),sep="")
