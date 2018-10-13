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
	
	input = [int(x) for x in line.split(' ')]
	
	old_limit = input[0]
	new_limit = input[1]
	pick_limit = input[2]
	
	winning_picks = 0
	
	if old_limit > new_limit:
		diff = old_limit - new_limit
		limit = old_limit - diff
		for i in range(limit):
			for j in range(i, limit):
				tmp = i & j
				if tmp < pick_limit:
					if i == j:
						winning_picks += 1
					else:
						winning_picks += 2
				
		for i in range(new_limit, old_limit):
			for j in range(new_limit):
				tmp = i & j
				if tmp < pick_limit:
					winning_picks += 1
	
	elif old_limit < new_limit:
		diff = new_limit - old_limit
		limit = new_limit - diff
		for i in range(limit):
			for j in range(i, limit):
				tmp = i & j
				if tmp < pick_limit:
					if i == j:
						winning_picks += 1
					else:
						winning_picks += 2
		
		for i in range(old_limit, new_limit):
			for j in range(old_limit):
				tmp = i & j
				if tmp < pick_limit:
					winning_picks += 1

		
				
	else:
		for i in range(old_limit):
			for j in range(i, old_limit):
				tmp = i & j
				if tmp < pick_limit:
					if i == j:
						winning_picks += 1
					else:
						winning_picks += 2
	
	
	
	print("Case #" + str(case) + ": " + str(winning_picks))
	