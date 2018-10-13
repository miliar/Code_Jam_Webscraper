#!/usr/bin/python
import itertools
import operator

lines = open('./C-small-attempt2.in').readlines()[1:]

lines.reverse()

case = 0
while lines:
	case += 1
	lines.pop()
	if not lines:
		break
	candies = [int(c) for c in lines.pop().split()]
	candies.sort()
	pats = []
	seans = []
	success = False
	for npat in range(len(candies))[1:]:
		iter = itertools.combinations(candies, npat)
		while True:
			try:
				pats = iter.next()
				seans = list(candies)
				[seans.remove(p) for p in pats]

				pat_value = reduce(operator.xor, pats, 0)
				sean_value = reduce(operator.xor, seans, 0)

				if pat_value == sean_value:
					success = True
					break

			except StopIteration:
				break

		if success:
			break

	if success == True:
		pat_value = reduce(operator.xor, pats, 0)
		sean_value = reduce(operator.xor, seans, 0)
		candies.sort()
		new_candies = seans + list(pats)
		new_candies.sort()
		assert new_candies == candies
		assert pat_value == sean_value
		assert sum(seans) >= sean_value
		assert sum(seans) <= sum(candies)
		result = sum(seans)
	else:
		result = 'NO'


	print "Case #%d: %s" % (case, result)
