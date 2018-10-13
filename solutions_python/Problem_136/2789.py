fil = open("B-large.in", 'r')
g = open("output.out", 'w')
cases = int(fil.readline())
i = 0

while i<cases:

 	i = i+1
	raw = fil.readline()
	c = float(raw.split()[0]) #500
	f = float(raw.split()[1]) #4
	x = float(raw.split()[2]) #2000

	if ((x/2) < ((c/2)+(x/(f+2)))):
		g.write("Case #" + str(i) + ": " + str(x/2) + "\n")

	else:
		flag = True
		counter = 0
		result = -1
		intermedio1 = 0
		intermedio2 = 0
		value1 = 0
		value2 = 0
		while flag:
			counter = counter + 1
			intermedio2 = intermedio2 + (c/(((counter)*f)+2))

			if (counter == 1):
				value1 = ((c/2) + 0 + (x/((counter*f)+2)))
			else:
				value1 = value2
			value2 = ((c/2) + intermedio2 + (x/(((counter+1)*f)+2)))

			# print "******"
			# print intermedio1
			# print intermedio2
			# print value1
			# print value2
			if (value1 < value2):
				#print "hola!"
				flag = False
				g.write("Case #" + str(i) + ": " + str(value1) + "\n")


	# if count == 1:
	# 	g.write("Case #" + str(i) + ": " + str(answer) + "\n")
	# elif count > 1:
	# 	g.write("Case #" + str(i) + ": " + "Bad magician!" + "\n")
	# else:
	# 	g.write("Case #" + str(i) + ": " + "Volunteer cheated!" + "\n")