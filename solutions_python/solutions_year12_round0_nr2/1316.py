fi = open("jamtestbig.txt","r")
fo = open("jamoutbig.txt","w")


lines = fi.readlines()
lines = lines[1:len(lines)]
case = 1

for line in lines : 
	samp = line.strip()
	s = samp.split(" ")
	sups = int(s[1])
	lim = int(s[2])
	scores = s[3:len(s)]
	aboves = 0
	
	for score in scores:
		score = int(score)
		if lim == 0 and score == 0:
			aboves = aboves + 1
		if score % 3 == 0 and score != 0:
			if (score/3) >= lim :
				aboves = aboves + 1
			elif (score == (lim+lim-1+lim-2))and(sups>0):
				sups = sups - 1
				aboves = aboves + 1			
		elif score % 3 == 1:
			if (((score-1)/3)+1) >= lim :
				aboves = aboves + 1

		elif score % 3 == 2:
			if (((score-2)/3)+1) >= lim :
				aboves = aboves + 1
			elif (score == (lim+lim-2+lim-2))and(sups>0):
				sups = sups - 1
				aboves = aboves + 1



	fo.write("Case #" + str(case) + ": " + str(aboves) + "\n")
	case = case + 1

fo.close()