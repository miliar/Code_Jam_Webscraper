Cases = int(input())
for Case in range(Cases):
	n, p = map(int,input().split())
	g = list(map(int,input().split()))
	n = len(list(g))

	#p = 4
	#g = g[:8]

	b = 0
	r = [0]*5
	for i in range(len(g)):
		g[i] %= p
		r[g[i]] += 1
	
	if p == 2:
		b = r[0] + (r[1]+1)//2
	elif p == 3:
		b = r[0]
		t = min(r[1],r[2])
		r[2] -= t
		r[1] -= t
		b += t
		b += (r[1]+2)//3
		b += (r[2]+2)//3
	elif p == 4:
		b = r[0]
		t = min(r[1],r[3]) # 3 1
		r[3] -= t
		r[1] -= t
		b += t
		t = min(r[2],r[3]//2) # 3 3 2
		r[3] -= 2*t
		r[2] -= t
		b += t
		t = r[3]//4 # 3 3 3 3
		r[3] -= 4*t
		b += t

		t = min(r[2],r[1]//2) # 2 1 1
		r[1] -= 2*t
		r[2] -= t
		b += t

		t = r[2]//2 # 2 2
		r[2] -= 2*t
		b += t

		if r[3] >= 1:
			b += 1
		else:
			if r[2] == 1:
				b += 1
			else:
				b += (r[1]+3)//4
	else:
		print('bad')

	print('Case #%d: %d' % (Case+1, b))