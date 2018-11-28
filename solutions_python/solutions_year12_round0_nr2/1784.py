import math
import sys

with open(sys.argv[1]) as input:
	input.next()
	for case, line in enumerate(input, 1):
		data = map(int, line.strip().split(' '))
		dancers, surprises, min_score = data[:3]
		scores = data[3:]
		
		result = 0
		scores.sort(reverse=True)
		for score in scores:
			if min_score > score:
				continue
			if math.ceil(score/3.0) >= min_score:
				result += 1
			elif score % 3 == 2 and score // 3 + 2 >= min_score and surprises:
				result += 1
				surprises -= 1
			elif score % 3 == 0 and score // 3 + 1 >= min_score and surprises:
				result += 1
				surprises -= 1
		
		print 'Case #%s: %s' % (case, result)