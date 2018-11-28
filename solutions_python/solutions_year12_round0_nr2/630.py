# Katja Collier
# Google Code Jam 2012, Qualification Round, Problem B. Dancing Googlers

import sys

def topScore(total, surprise) :
	average = float(total)/3.0
	if total == 0 :
		return total
	elif surprise :
		# calculate highest possible score if low and high can be 2 apart
		if (average % 1.0) < .5 :
			return int(average) + 1
		else  :
			return int(average) + 2
			
		
			"""
			# total - avg - best
			
			# 1 ----> 0 ---> 1
			# 2 ----> 0 ---> 2
			
			# 4 ----> 1 ---> 2 
			# 5 ----> 1 ---> 3 
		
			# 7 ----> 2 ---> 3
			# 8 ----> 2 ---> 4 
			"""
			
	else :
		# "" if low and high can be 1 apart
		if average % 1.0 == 0 :
			return int(average)
		else :
			return int(average) + 1
			

		

# Main code:

# read input - each row goes into list of integers
# list is called triplets



file = sys.stdin
lines = []
for l in file :
	lines.append(l)

k = 1
while k < len(lines) :
	counter = 0
	triplets = map(int, lines[k].split())
	numSurprises = triplets[1]
	minResult = triplets[2]
	
	
	i = 3
	while i < len(triplets) :
		firstTry = topScore(triplets[i], False)
		if firstTry >= minResult :
			counter += 1
		elif numSurprises > 0 :
			secondTry = topScore(triplets[i], True) 
			if secondTry >= minResult :
				counter += 1
				numSurprises -= 1
		i += 1
	
	
	print "Case #%d: %d" % (k, counter)
	k += 1
	
	
