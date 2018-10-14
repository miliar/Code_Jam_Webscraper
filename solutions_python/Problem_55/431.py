t = int(raw_input())
case = 1

while t-case+1:
	rkn = raw_input().split(' ')
	r = int(rkn[0])
	k = int(rkn[1])
	n = int(rkn[2])
	gs = raw_input().split(' ')
	
	count = []
	g = []
	
	for i in range(0,n):
		g.append(int(gs[i]))
	
	end = []
	m = []
	
	for i in range(0,n):
		count = g[i]
		s = (i + 1) % n
		e = i
		while (count + g[s] <= k) and (s != i):
			count = count + g[s]
			e = s
			s = (s + 1) % n
		end.append(e)
		m.append(count)

	head = 0
	money = 0
			
	while r:
		r = r - 1
		money = money + m[head]
		head = (end[head] + 1) % n
	
	print 'Case #%i: %i' % (case, money)
	case = case + 1