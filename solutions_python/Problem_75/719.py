input = open("B-large.in")
output = open("B-large.out", 'w')

lines = input.readlines()

num_cases = int(lines.pop(0))

for case in range(num_cases):
	
	#parse input
	line = lines[case].split(' ')
	
	num_combinations = int(line.pop(0))
	combinations = []
	for combination in range(num_combinations):
		combinations.append(line.pop(0))
	
	num_oppositions = int(line.pop(0))
	oppositions = []
	for opposition in range(num_oppositions):
		oppositions.append(line.pop(0))
		
	num_elements = int(line.pop(0))
	elements = list(line.pop(0).rstrip('\n'))
	
	
	
	#compute final string
	result = []
	#print "case: " + str(case)
	#print "elements: " + str(elements)
	for e in elements:
		#print "e: " + e
		#print "result at step: " + str(result)
		#check for combination
		did_combine = False
		if len(result) > 0:
			last = result[len(result) - 1]
			#print "last:" + last + " e:" + e
			for combination in combinations:
				if (not did_combine) and ((combination[0] == e and combination[1] == last) or (combination[0] == last and combination[1] == e)):
					result.pop()
					result.append(combination[2])
					did_combine = True
					#print "COMBINED! last:" + last + " e:" + e + " combination:" + combination
				 
				
		#check for opposition
		did_oppose = False
		if not did_combine:
			for opposition in oppositions:
				for r in result:
					if (opposition[0] == r and opposition[1] == e) or (opposition[0] == e and opposition[1] == r):
						result = []
						did_oppose = True
						#print "OPPOSED! r:" + r + " e:" + e + " opposition:" + combination
						
		
		if (not did_combine) and (not did_oppose):
			result.append(e)
	
	#write output		
	output.write("Case #" + str(case+1) + ": [")
	for i in range(len(result)):
		w = result[i]
		if i != len(result) - 1:
			w += ', '
		output.write(w)
	output.write("]\n")
	#print ""				