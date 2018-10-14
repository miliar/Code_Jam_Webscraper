f = open('q1.in', 'r')
f1 = open('q1.out', 'w')
no_cases = f.readline().strip()
for x in range(0, int(no_cases)):
	num  = f.readline().strip()
	for y in range(0, 4):
		grid  = f.readline()
		if y+1 == int(num):
			set1 = grid.split()

	num2  = f.readline().strip()
	for y in range(0, 4):
		grid  = f.readline()
		if y+1 == int(num2):
			set2 = grid.split()

	output = list(set(set1).intersection( set(set2)))
	h = str(x+1)
	if len(output) == 1:
		f1.write("Case #"+h+": "+output[0]+"\n")
	elif len(output) == 0:
		f1.write( "Case #"+h+": Volunteer cheated!\n")
	else:
		f1.write( "Case #"+h+": Bad magician!\n")
