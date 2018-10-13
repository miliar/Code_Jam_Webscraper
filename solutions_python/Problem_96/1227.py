import sys

#Given a number, construct a triple of scores
#that is as unsurprising as possible.
def unsurprise(number):
	average = number/3
	if (number % 3 == 0):
		return [average,average,average]
	else:
		b = average+1
		c = number - average - b
		return [average,b,c]
		
#Given a triple of scores, returns True if it
#can be converted to a surprising pair and False
#otherwise		
def surprisable(scores):
	#If there are two or more copies of the best score
	#in scores, scores will be surprisable.  if there
	#is only one copies of the best score, then trying
	#to create a surprising score closer to p will instead
	#create an invalid pair
	best = max(scores)
	if(scores.count(best) >= 2):
		return True
	return False

#Returns a surprising version of scores; a valid
#pair that sums to the same vale of score, but is
#also a surprising score.  Assuming input is unsurprising.	
def surprise(scores):
	best = max(scores)
	newScores = [best+1,best-1,sum(scores)-best-best]
	
	#Make sure surprise version is within reasonable bounds
	for i in newScores:
		if (i<0 or i>10):
			return scores
	
	return newScores
	

#Return true if the best result for a set
#of score meets or exceeds the value best_score		
def best_at_least_p(scores,best_score):
	for i in scores:
		if i >= best_score:
			return True
	return False
	
def best_value_comparator(scores):
	if max(scores) == 0:
		return 0
	return sum(scores)/float(max(scores))
	
	
if (len(sys.argv) > 1):
	file = open(sys.argv[1],'r')
	outfile = open("output", 'w')
	cases = file.readline()
	cases = int(cases)
	iters = 0
	
	while(iters < cases):
		#Read data
		data = file.readline()
		data = data.split(' ')
		for i in range(len(data)):
			data[i] = int(data[i])
			
		#Now create unsurprising pairs from data, then check how many
		#unsurprising pairs have scores that exceed p
		
		pairs = [unsurprise(x) for x in data[3:len(data)+data[0]]]
		
		#Sort pairs by their best values; those with higher best vales have
		#better chance of meeting p when converted to surprising pairs
		pairs = sorted(pairs, key=best_value_comparator, reverse=True);
		answer = 0
		
		for scores in pairs:
			if(best_at_least_p(scores,data[2])):
				answer += 1
			else:
				if(surprisable(scores) and data[1] > 0):
					if(best_at_least_p(surprise(scores),data[2])):
						data[1] -= 1
						answer += 1
					else:
						continue
				else:
					continue
					
		outfile.write("Case #" + str(iters+1) + ": " + str(answer) + '\n')
		
		iters += 1
	
	
	file.close()
	outfile.close()