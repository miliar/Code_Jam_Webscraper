myfile = open("B-large.in", "r")
myfile2 = open("output.txt", "w")

a = 111111111111111110
b = str(a)

#print a
case = 0
myfile.readline()
for line in myfile:
	a = int(line)
	b = line
	case+=1
	x = a
	while x>=0:
		#print x
		b = str(x)
		c = 0
		flag = 1
		counter = len(str(x))
		for y in b:

			if y >= c:
				c = y
			else:
				flag = 0
				#print x%(10**counter), "this is x"
				x-=x%(10**counter)
			counter-=1
		if flag == 1:
			#print x
			if case != 1:
				myfile2.write("\n")
			myfile2.write("Case #")
			myfile2.write(str(case))
			myfile2.write(": ")
			myfile2.write(str(x))
			#print "wooho"
			break

		x-=1

