
T = int(raw_input())

'''
for i in range(1, T+1):
	R, k, N = tuple(map(lambda x : int(x), raw_input().split()))
	gs = map(lambda x : int(x), raw_input().split())
	res = 0
	for l in xrange(R):
		nbgroups = 0
		rem_seats = k
		while nbgroups < N and gs[0] <= rem_seats:
			rem_seats -= gs[0]
			nbgroups += 1
			res += gs[0]
			gs.append(gs[0])
			del gs[0]
	print 'Case #%d: %d' % (i, res)
'''

def compute_money_pos(start, groups, k):
	pos = start
	rem_k = k
	
	while (pos != start or rem_k == k) and rem_k >= groups[pos]:
		rem_k -= groups[pos]
		pos = (pos + 1) % len(groups)
	
	return k - rem_k, pos

for i in range(1, T+1):
	R, k, N = tuple(map(lambda x : int(x), raw_input().split()))
	gs = map(lambda x : int(x), raw_input().split())
	res = 0
	
	# cas trivial
	dyn = {}
	for pos in range(len(gs)):
		dyn[1, pos] = compute_money_pos(pos, gs, k)
	# constructions intermediaires
	for ndim in range(2, 101):
		for pos in range(len(gs)):
			m1, p1 = dyn[ndim-1, pos]
			m2, p2 = dyn[1, p1]
			dyn[ndim, pos] = m1+m2, p2
	
	# attaque de la boucle :D
	rem_R = R
	pos = 0
	money = 0
	while rem_R:
		nb_rc = min(100, rem_R)
		m, pos = dyn[nb_rc, pos]
		
		money += m
		rem_R -= nb_rc
	
	print 'Case #%d: %d' % (i, money)

	