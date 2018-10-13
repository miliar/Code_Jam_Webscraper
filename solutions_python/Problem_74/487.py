############# GOOGLE CODE JAM 2011 ################


###################################################
#QUALIFICATION ROUND
###################################################
def portal_problem(filename):

	### First I will construct a useful data structure
	### from the input
	### this will be a list of test cases
	### where each test case is a list of instructions
	### where each instruction is a tuple
	### i.e. [[('O',1),('B',5)...],[('B',100),('O',1)...]...]
	data = read_in_data(filename)
	
	file = open('output.log', 'w')
	
	for case in xrange(len(data)):
		time = solve_test(data[case])
		file.write('Case #')
		file.write(str(case+1))
		file.write(': ')
		file.write(str(time))
		file.write('\n')
		
	file.close()
	
	
	
def read_in_data(filename):
	file = open(filename)
	x = int(file.readline())	### x is the number of test cases
	data = []
	for i in range(x):
		
		case = []
		templine = file.readline()
		templine = templine.split()
		
		for j in range(0,len(templine)-2,2):
			case.append((templine[j+1],int(templine[j+2])))
			
		data.append(case)
		
	file.close()
		
	return data
	
def solve_test(test_case):
	
	### create the list of actions for the robots
	### initialized to 1 because they start at position 1 at time 0
	orange = [1] 
	blue = [1]
	
	push_time = 0
	
	
	while len(test_case) > 0:
		
		instruction = test_case.pop(0)
		
		
		
		### choose which list we will be modifying based on the robot currently
		### asked to do something
		if instruction[0] == 'O':
			robot = orange		
		else:
			robot = blue
		
		
		
		
		### If the robot is already in position
		### just wait until the other robot has pressed the button
		if instruction[1] == robot[len(robot)-1]:
		
			while len(robot)-1 < push_time: ### if the other robot hosn't pushed yet
				robot.append(robot[len(robot)-1])
				
			robot.append(instruction[1])			
		
		
		
		
		
		### If the robot is not in position
		### move it into position then wait
		### until other robot has pressed the button
		else:
			move_robot(instruction,robot)
			
			while len(robot)-1 < push_time: ### if the other robot hosn't pushed yet
				robot.append(robot[len(robot)-1])
				
			robot.append(instruction[1])
			
		
		
		
		### set the new push time
		push_time = len(robot)-1
		
	
	
	
	### Once we have gone through all of the instructions
	### the action list belonging to the robot who did the last
	### instruction will contain the full lenth so we need to return
	### that time
	
	return len(robot)-1
	

def move_robot(instruction,robot):
	'''
	if a robot is not in position, this is called
	to move the robot to the right button
	'''
	
	### First we will handle the case where the robot isn't far enough
	while robot[len(robot)-1] < instruction[1]:
		
		robot.append(robot[len(robot)-1]+1)
		
	
	### Next is when the robot is too far
	while robot[len(robot)-1] > instruction[1]:
		
		robot.append(robot[len(robot)-1] - 1)
	
			
			
			
			
		
		
		