
infile = raw_input("File: ")
lines = open(infile, 'r').readlines()
output = open(infile[:-3]+"_solution"+infile[-3:], "w")

T = lines.pop(0)
counter = 1
for line in lines:
	numbers = line.split()
	N = int(numbers.pop(0)) #number of numbers
	S = int(numbers.pop(0)) #number of surprises
	p = int(numbers.pop(0)) #number of target
	total = 0
	for number in numbers:
		scorebase = int(number) // 3
		remainder = int(number) %  3
		if remainder == 0:   #score = (scorebase, scorebase, scorebase)
			if scorebase >= p:   # = (scorebase-1, scorebase, scorebase+1)
				total += 1
				continue
			elif scorebase+1 >= p and S > 0 and scorebase>0:
				total += 1
				S -= 1
				continue
		elif remainder == 1: #score = (scorebase, scorebase, scorebase+1)
			if scorebase+1 >= p:
				total += 1
				continue
		elif remainder == 2: #score = (scorebase, scorebase, scorebase+2)
			if scorebase+1 >= p: # = (scorebase, scorebase+1, scorebase+1)
				total += 1
				continue
			elif scorebase+2 >= p and S > 0:
				total += 1
				S -= 1
				continue
	output.write("Case #"+str(counter)+": "+str(total)+"\n")
	counter += 1
