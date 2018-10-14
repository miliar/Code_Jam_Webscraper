T = int(input())
for t in range(T):
	line = input().split()
	A = int(line[0])
	B = int(line[1])
	
	p = []
	for l in input().split():
		p.append(float(l))
	zero = []
	for i in range(A):
		if p[i]==0:
			zero.append(i)
	zero.append(A)
	begin = zero[0]
	base = B+2
	best = A-begin+B-begin+1
	while best < base:
		ok = 1
		for b in range(begin):
			ok *= p[b]
		now = ok*best+(1-ok)*(best+B+1)
		if now < base:
			flag = True
			base = now
		begin -= 1
		best = A-begin+B-begin+1
	print("Case #" + str(t+1) + ": " + str(base))
