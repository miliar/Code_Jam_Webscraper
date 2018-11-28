filename = raw_input("filename: " )
f = open(filename, "r")
g = open("A.out", "w")
num_tests = int(f.readline().rstrip())
LINES = 4
result1 = "Bad magician!"
result2 = "Volunteer cheated!"
results = []
for i in range(num_tests):
	line_number = int(f.readline().rstrip())
	for i in range(line_number):
		current_line = f.readline().rstrip()
	cards1 = current_line.split()
	for i in range(LINES - line_number):
		current_line = f.readline()
	line_number = int(f.readline().rstrip())
	for i in range(line_number):
		current_line = f.readline().rstrip()
	cards2 = current_line.split()
	for i in range(LINES - line_number):
		current_line = f.readline()	
	common = list(set(cards1).intersection(cards2))
	if len(common) == 1:
		results.append(common[0])
	elif len(common) == 0:
		results.append(result2)
	else:
		results.append(result1)
for i in range(num_tests):
	current_result = "Case #" + str(i+1) + ": " + results[i]
	g.write(current_result)
	if i < num_tests:
		g.write("\n")
f.close()
g.close()