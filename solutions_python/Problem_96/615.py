import sys

def tg():
	for x in xrange(11):
		for y in xrange(11):
			if abs(x - y) > 2: continue
			for z in xrange(11):
				if abs(x - z) > 2: continue
				if abs(y - z) > 2: continue
				yield (x, y, z)

plain_best = {}
surprizing_best = {}
for triple in tg():
	x,y,z=triple
	total = sum(triple)
	best = max(triple)
	surprizing = abs(x-y) == 2 or abs(x-z) == 2 or abs(y-z) == 2
	if surprizing:
		if total not in surprizing_best or best > surprizing_best[total]:
			surprizing_best[total] = best
	else:
		if total not in plain_best or best > plain_best[total]:
			plain_best[total] = best

def count(surprizes, goal, scores):
	result = 0
	for s in scores:
		if plain_best[s] >= goal: 
			result += 1
		elif surprizes > 0 and s in surprizing_best and surprizing_best[s] >= goal:
			result += 1
			surprizes -= 1
	return result

f = open(sys.argv[1], 'r')
i = -1
for l in f:
	i += 1
	if i == 0: continue
	v = [int(x) for x in l.split()]
	print "Case #%d: %d"%(i, count(v[1], v[2], v[3:]))