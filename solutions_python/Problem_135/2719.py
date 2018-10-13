inputfile = open('A-small-attempt0.in', 'r')
outputfile = open('A-small-attempt0.out', 'w')
t = int(inputfile.readline())
for i in range(t):
	s1 = set()
	s2 = set()
	r1 = int(inputfile.readline())
	for j in range(4):
		line = inputfile.readline()
		if j+1 == r1:
			s1 = set(line.split())
	r2 = int(inputfile.readline())
	for j in range(4):
		line = inputfile.readline()
		if j+1 == r2:
			s2 = set(line.split())
	s = s1 & s2
	outputfile.write("Case #" + str(i+1) + ": ")
	if len(s) == 0:
		outputfile.write("Volunteer cheated!")
	elif len(s) == 1:
		outputfile.write(s.pop())
	else:
		outputfile.write("Bad magician!")
	outputfile.write('\n')
outputfile.close()
	
