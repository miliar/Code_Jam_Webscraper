import math 

def solve(raw):

	raw_list = raw.split(' ')
	specs = int(raw_list[1])
	best = int(raw_list[2])
	scores = [int(x) for x in raw_list[3:]]
	can_score = 0

	for x in scores:
		if x >= best:
			x -= best

			if (best-math.floor(x/2.0)) <= 1:
				can_score += 1
			elif (best-math.floor(x/2.0)) <= 2 and specs > 0:
				can_score += 1
				specs -= 1

	return can_score


for x in range(input()):
	print "Case #" + str(x+1) + ": " + str(solve(raw_input()))
