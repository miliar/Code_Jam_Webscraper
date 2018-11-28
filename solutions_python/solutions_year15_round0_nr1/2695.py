file = open("A-large.in")
output = open("A-large.out", 'w')
cases = eval(file.readline())

for case in range(cases):
	input_line = file.readline().rstrip().split(" ")
	maxshyness = int(input_line[0])
	people = [int(x) for x in input_line[1]]
	needed_people = 0
	current_standing = 0 
	for i in range(0, maxshyness + 1):
		if people[i] > 0:
			if current_standing < i:
				needed_people += i - current_standing
				current_standing += (i - current_standing) + people[i]
			else: 
				current_standing += people[i]
				
	output.write("Case #" + str(case + 1) + ": " + str(needed_people) + "\n")