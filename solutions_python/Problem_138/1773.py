dump = open('DS.in', 'r').readlines()

test_cases = int(dump[0][:-1])

data = zip([map(float, x[:-1].split(' ')) for x in dump[2:][::3]], [map(float, x[:-1].split(' ')) for x in dump[3:][::3]])

for t in xrange(test_cases):
	print 'Case #{}:'.format(t+1),
	
	dwar_n = [x for x in data[t][0]]
	dwar_k = [x for x in data[t][1]]
	dwar_ns = 0
	
	while dwar_n:
		win = [x for x in dwar_n if x > max(dwar_k)]
		lose = [x for x in dwar_n if x < min(dwar_k)]
		n = [x for x in dwar_n if x < max(dwar_k) and x > min(dwar_k)]
		if n:
			dwar_n.remove(min(n))
			dwar_k.remove(min(dwar_k))
			dwar_ns +=1
		
		else:
			if lose:
				dwar_n.remove(min(lose))
			else:
				dwar_n.remove(min(win))
				dwar_ns += 1
			dwar_k.remove(min(dwar_k))
	print dwar_ns,

	war_n = sorted([x for x in data[t][0]])
	war_k = [x for x in data[t][1]]
	war_ns = 0
		
	while war_n:
		nm = war_n.pop()
		if max(war_k) > nm:
			war_k.remove(max(war_k))
		else:
			war_k.remove(min(war_k))
			war_ns += 1
	print war_ns

