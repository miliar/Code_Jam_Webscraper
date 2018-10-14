

filein = open('C-large.in')
fileout = open('output.txt', 'w')

line_no = 0

for line in filein:
	line_no += 1
	
	if not line_no == 1:
		numbers = line.split()
		
		lower_limit = int(numbers[0])
		upper_limit = int(numbers[1])
		number_of_pairs = 0
		pairs = []
		
		for i in xrange(lower_limit, upper_limit):
			curr = str(i)
			
			if len(curr) > 1:
				for n in xrange(0, len(curr)):
					if n > 0:
						first = curr[0:n + 1]
						last = curr[n + 1:len(curr)]
					else:
						first = curr[0]
						last = curr[n + 1:len(curr)] 
					
					new_curr = last + first
					new_num = int(new_curr)
					
					if new_num > i:
						if new_num <= upper_limit:
							pairs.append((i, new_num))
			
		number_of_pairs = len(set(pairs))
		fileout.write("Case #%d: %s\n" % (line_no - 1, number_of_pairs))

filein.close()
fileout.close()		


