import string
def prepare_data(data):
	numbers = data.split()
	N = int(numbers[0])
	s = int(numbers[1])
	p = int(numbers[2])
	points = [int(numbers[i]) for i in xrange(3, 3 + N )]
	return (N, s, p, points)

def canAchieveWithoutSurprises(points, best_result):
	best_score = 0
	if points % 3 == 0:
		best_score = points / 3
	elif points % 3 == 1:
		best_score = int(points / 3) + 1
	elif points % 3 == 2:
		best_score = int(points / 3) + 1
	
	return best_score >= best_result
def canAchieveWithSurprises(points, best_result):
	if points == 0:
		return best_result == 0
	best_score = 0
	if points % 3 == 0:
		best_score = points / 3 + 1
	elif points % 3 == 1:
		best_score = int(points / 3) + 1
	elif points % 3 == 2:
		best_score = int(points / 3) + 2
	
	return best_score >= best_result

def solve(data):
	N, s, p, points = prepare_data(data)
	result = 0
	for x in points:
		if canAchieveWithoutSurprises(x, p):
			result += 1
		elif s > 0 and canAchieveWithSurprises(x, p):
			s -= 1
			result += 1

	return result

if __name__ == '__main__':
	import sys
	T = int(sys.stdin.readline())
	for i in xrange(T):
		input_str = sys.stdin.readline().strip()
		res = solve(input_str)
		print "Case #%d: %s" % (i + 1, res)	

