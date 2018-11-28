INPUT = 'A-small-attempt0.in'
OUTPUT = 'A-small-attempt0.out'

with open(INPUT, 'r') as f:
	outputf = open(OUTPUT, 'w')
	current_case = 0

	for i, line in enumerate(f):
		if i > 0:
			current_case += 1
			friends = 0
			stand = 0
			max_level = int(line[0])
			
			all_levels = line[2:]
			
			for p in range(max_level+1):

				if p == 0:
					stand += int(all_levels[0])
					continue
				if ((p > stand) and (int(all_levels[p]) > 0)):
					
					
					friends += p - stand 
					stand += int(all_levels[p]) + p - stand 
					
				else:
					stand += int(all_levels[p])
			line = 'Case #' + str(current_case) + ': ' + str(friends) + '\n'		
			
			outputf.write(line)		
				
						

			