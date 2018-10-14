import sys

def bestscore(score, gap=1):
	"""
	Will work out best score with total as score...
	"""
	
	for n in [10,9,8,7,6,5,4,3,2,1,0]:
		rem = score-n
		if rem < 0:
			continue
		
		#remaining needs splitting into two lower amounts..
		hrem = rem/2 # will round down
			# 3/2 = 1 ; 3 = 1+2...
			# 5/2 = 2 ; 5 = 2+3...
		
		pgap = n-hrem
		
		if pgap <= gap:
			return n
	
	return 0
		


def question(S, p, scores):

	result = 0
	sleft = S
	
	for score in scores:
		bns = bestscore(score, gap=1)
		if bns >= p:
			result += 1
		elif sleft > 0:
			bws = bestscore(score, gap=2)
			
			if bws >= p:
				result += 1
				sleft -= 1
	
	return result
			
		


f = file(sys.argv[1], "r")
fo = file(sys.argv[2], "w")

#fo.write("Output\r\n")
i = 1

for line in f:
	line = line.strip()
	if line == "Input":
		continue
	try:
		int(line)
		continue
	except:
		pass
	
	
	#Do the Magic!
	parts = line.split(" ")
	iparts = []
	for part in parts:
		iparts.append(int(part))
		
	N = iparts[0] # Total Number
	S = iparts[1] #Surpise!
	p = iparts[2] #max score
	scores = iparts[3:]
	if len(scores) != N:
		print "wtf..."
		
	
	ans = question(S, p, scores)
	
	fo.write("Case #"+str(i)+": "+str(ans)+"\r\n")
	i += 1

fo.close()
f.close()
