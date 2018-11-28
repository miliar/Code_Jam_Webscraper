t = input()

for i in range(t):
	l = raw_input().split()
	n = int(l.pop(0))
	robots = { 'O':[], 'B':[] }
	turns = []
	for j in range(n):
		r = l.pop(0)
		robots[r].append(int(l.pop(0)))
		turns.append(r)
	position = {'O':1, 'B':1}
	cost = 0
	turn = turns.pop(0)
	while len(robots['O']) > 0 and len(robots['B']) > 0:
		cost += 1
		if position['O'] == robots['O'][0] and turn == 'O':
			robots['O'].pop(0)
			turn = turns.pop(0)
			if robots['B']:
				if position['B'] > robots['B'][0]:
					position['B'] -= 1
				elif position['B'] < robots['B'][0]:
					position['B'] += 1
		elif position['B'] == robots['B'][0] and turn == 'B':
			turn = turns.pop(0)
			robots['B'].pop(0)
			if robots['O']:
				if position['O'] > robots['O'][0]:
					position['O'] -= 1
				elif position['O'] < robots['O'][0]:
					position['O'] += 1
		else:
			if position['B'] > robots['B'][0]:
				position['B'] -= 1
			elif position['B'] < robots['B'][0]:
				position['B'] += 1
		
			if position['O'] > robots['O'][0]:
				position['O'] -= 1
			elif position['O'] < robots['O'][0]:
				position['O'] += 1
	while robots['B']:
		nextPos = robots['B'].pop(0)
		cost += abs(position['B'] - nextPos) + 1
		position['B'] = nextPos
	while robots['O']:
		nextPos = robots['O'].pop(0)
		cost += abs(position['O'] - nextPos) + 1
		position['O'] = nextPos
	print "Case #%d: %d" % (i+1, cost)
