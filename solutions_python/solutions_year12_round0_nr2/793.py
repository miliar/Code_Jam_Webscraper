

filein = open('B-small-attempt0.in')
fileout = open('output.txt', 'w')

line_no = 0

for line in filein:
	line_no += 1
	
	if not line_no == 1:
		numbers = line.split()
		
		googlers = int(numbers[0])
		surprises = int(numbers[1])
		threshold = int(numbers[2])
		nice_score = 0
		
		sorted_scores = [int(numbers[i]) for i in xrange(3, 3 + googlers)]
		sorted_scores.sort()
		sorted_scores.reverse()
		
		print(sorted_scores)
		
		for score in sorted_scores:
			if score / 3 >= threshold:
				nice_score += 1
			elif abs((score / 3) - threshold) > 2:
				pass
			else:
				if not score == 0:
					if score % 3 > 0:
						if (score / 3 + 1 >= threshold):
							nice_score += 1
						elif (score / 3 + 2 >= threshold) and surprises > 0:
							nice_score += 1
							surprises -= 1
					elif (score % 3 == 0 and surprises > 0):
						if (score / 3 + 1 >= threshold):
							nice_score += 1
							surprises -= 1
				
		
		fileout.write("Case #%d: %s\n" % (line_no - 1, nice_score))

filein.close()
fileout.close()		


