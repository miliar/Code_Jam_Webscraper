input = open("A-large.in")
output = open("A-large.out", 'w')

lines = input.readlines()

num_cases = int(lines[0])

for case in range(num_cases):
	
	#interpret input line
	line = lines[case+1].split(' ')
	#print "line:" + line
	
	num_steps = int(line[0])
	#print "num_steps:" + str(num_steps)
	
	steps = []
	
	for i in range(num_steps):
		step = (line[i*2+1], int(line[i*2+2]))
		steps.append(step)
		
	#print "steps:" + str(steps)
	
	
	#calculate number of seconds needed
	orange_position = 1
	blue_position = 1
	
	orange_target = 1
	blue_target = 1
	
	blue_target_found = False
	orange_target_found = False
	
	for i in range(len(steps)):
		
		if not blue_target_found and steps[i][0] == 'B':
			blue_target = steps[i][1]
			blue_target_found = True
			#print "blue_target:" + str(blue_target)
		
		if not orange_target_found and steps[i][0] == 'O':
			orange_target = steps[i][1]
			orange_target_found = True
			#print "orange_target:" + str(orange_target)
	
	time = 0
	
	while len(steps) > 0:
	
		time += 1
		button = False
		
		#print "time:" + str(time)
		
		if steps[0][0] == 'O' and orange_position == steps[0][1]:
			button = True
			#print "orange: press button"
		else:
			if orange_position < orange_target:
				orange_position += 1
				#print "orange: move to " + str(orange_position)
			elif orange_position > orange_target:
				orange_position -= 1
				#print "orange: move to " + str(orange_position)
			#else:
				#print "orange: stay at " + str(orange_position)
					
		if steps[0][0] == 'B' and blue_position == steps[0][1]:
			button = True
			#print "blue: press button"
			
		else:
			if blue_position < blue_target:
				blue_position += 1
				#print "blue: move to " + str(blue_position)
			elif blue_position > blue_target:
				blue_position -= 1
				#print "blue: move to " + str(blue_position)
			#else:
				#print "blue: stay at " + str(blue_position)
		
		if button:
			steps.pop(0)
			#print "steps:" + str(steps)
			if len(steps) > 0:
				orange_target_found = False
				blue_target_found = False
				
				for i in range(len(steps)):
					
					if not blue_target_found and steps[i][0] == 'B':
						blue_target = steps[i][1]
						blue_target_found = True
						#print "blue_target:" + str(blue_target)
					
					if not orange_target_found and steps[i][0] == 'O':
						orange_target = steps[i][1]
						orange_target_found = True
						#print "orange_target:" + str(orange_target)
		
		#print ""
		
		#raw_input()
				
	output.write("Case #" + str(case+1) + ": " + str(time) + "\n")
	#raw_input()
	
		
	