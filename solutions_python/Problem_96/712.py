#!/usr/bin/python

f = open("test.in")
count = 0
for line in f.readlines():
	total = 0
	line = line.strip()
	if count == 0:
		t = line
	else:
		# n = number of Googlers
		# s = number of surprises
		# p = Best Result (?)
		lineList = line.split()
		tempList = []
		possibleSurprises = 0
		n = lineList[0]
		s = int(lineList[1])
		p = lineList[2]
		lineList = lineList[3:]
#		print n, s, p, lineList
		# remove definite wins/loses
		for a in lineList:
			average = int(a)/3
			remainder = int(a)%3
			if average >= int(p):
				total += 1
			elif a == "0":
			    pass
			elif remainder == 0: 
				if (average + 1) >= int(p):
					possibleSurprises += 1
					tempList.append(a)
			elif remainder == 1:
				if (average + 1) >= int(p):
					total += 1
			elif remainder == 2:
				if (average + 1) >= int(p):
				    total += 1
				elif (average + 2) >= int(p):
					possibleSurprises += 1
					tempList.append(a)
			else:
				tempList.append(a)
		
				
				
				
#		print "Remaining: ", tempList
#		print "Potential Surprises", possibleSurprises
#		print "Known Surprises", s
		while possibleSurprises > 0 and s > 0:
			total += 1
			possibleSurprises -= 1
			s -= 1
#		print "Total: "+str(total)
#		print line
		print "Case #"+str(count)+":",total
	








	count += 1
	
