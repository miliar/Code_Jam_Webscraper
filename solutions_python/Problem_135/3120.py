f = open("./input.txt", 'r')
w = open("./output.txt", 'w')
numCases = f.readline()
for t in range(int(numCases)):
	ans1 = f.readline()
	options = []
	for i in range(4):
		s = f.readline()
		if i+1 == int(ans1):
			options = map(int, s.split())
	ans2 = f.readline()
	print(options)
	answers = []
	for i in range(4):
		s = f.readline()
		if i+1 == int(ans2):
			array2 = map(int, s.split())
			print array2
			for o in options:
				if (o in array2):
					answers.append(o)
	print(answers)
	w.write("Case #"+str(t+1)+": ")
	if len(answers) == 0:
		w.write("Volunteer cheated!\n")
	elif len(answers) == 1:
		w.write(str(answers[0])+"\n")
	else:
		w.write("Bad magician!\n")
f.close()
w.close()