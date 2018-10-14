with open('D-large.in') as f:
	data = f.readlines()
trials = int(data.pop(0).strip())

def choose(toBeat, blocks):
	for b in blocks:
		if b > toBeat:
			return b
	return blocks[0]

def war(naomi, ken):
	wins = 0
	for choseN in naomi:
		choseK = choose(choseN, ken)
		ken.remove(choseK)
		if choseN > choseK:
			wins += 1
	return wins

def deceit(naomi, ken):
	wins = 0
	lowK = ken[0]
	toBurn = 0
	for choseN in naomi:
		if choseN < ken[0]:
			tellN = ken[-1] - .00000001
		elif choseN > ken[0]:
			tellN = ken[-1] + .00000001
		choseK = choose(tellN, ken)
		ken.remove(choseK)
		if choseN > choseK:
			wins += 1
	return wins

for i in range(trials):
	num = int(data.pop(0))
	naomi = sorted([float(n) for n in data.pop(0).strip().split()])
	ke = sorted([float(n) for n in data.pop(0).strip().split()])

	print 'Case #{0}:'.format(i+1), deceit(naomi, ke[:]), war(naomi, ke[:])