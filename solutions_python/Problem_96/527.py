import sys
import math

index = 0
for line in open(sys.argv[1]).readlines()[1:]:
	index += 1
	numbers = map(float, line.split())
	n = numbers[0]
	s = numbers[1]
	p = numbers[2]
	total_scores = numbers[3:]
	num = 0
	for i, score in enumerate(total_scores):
		score1 = math.ceil(score / 3.0)
		score2 = math.ceil((score-score1) / 2.0)
		score3 = score-score1-score2
		if score1 >= p: num += 1
		elif score1 == p-1 and s > 0 and score1 == score2 and score2 != 0:
			num += 1
			s -= 1
			
	print "Case #%i: %i" % (index, num)
	
