import sys


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))


# Get total number of test cases
test_cases = int(lines[0])
del lines[0]

# Process each test case
case = 0
for line in lines:
	
	case += 1
	input = [float(x) for x in line.split(" ")]
	
	farm_cost = input[0]
	production_increase = input[1]
	goal = input[2]
	
	
	production = 2
	seconds = 0.0
	
	while (True):
		seconds_to_farm = farm_cost / production
		seconds_to_goal = goal / production
		seconds_to_goal_with_farm = seconds_to_farm + (goal / (production + production_increase))
		
		if seconds_to_goal < seconds_to_goal_with_farm:
			seconds += seconds_to_goal
			break
			
		else:
			seconds += seconds_to_farm
			production += production_increase
		
	print("Case #" + str(case) + ": " + str(seconds))