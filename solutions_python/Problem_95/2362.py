openfile = open('C:\Users\Andrew\Downloads\A-small-attemptz0.in', 'r')
out = open("C:\Users\Andrew\Desktop\output.txt", "w")
inputs = openfile.readlines()
inputs.pop(0)

case = 1
while len(inputs) > 0:
	string1 = list(inputs.pop(0))
	list1 = list()
	while len(string1) > 0:
		string3 = string1.pop(0)
		if string3 == ' ':
			list1.append(' ')
		if string3 == 'a':
			list1.append('y')
		if string3 == 'b':
			list1.append('h')
		if string3 == 'c':
			list1.append('e')			
		if string3 == 'd':
			list1.append('s')
		if string3 == 'e':
			list1.append('o')
		if string3 == 'f':
			list1.append('c')
		if string3 == 'g':
			list1.append('v')
		if string3 == 'h':
			list1.append('x')
		if string3 == 'i':
			list1.append('d')
		if string3 == 'j':
			list1.append('u')
		if string3 == 'k':
			list1.append('i')
		if string3 == 'l':
			list1.append('g')
		if string3 == 'm':
			list1.append('l')
		if string3 == 'n':
			list1.append('b')
		if string3 == 'o':
			list1.append('k')
		if string3 == 'p':
			list1.append('r')
		if string3 == 'q':
			list1.append('z')
		if string3 == 'r':
			list1.append('t')
		if string3 == 's':
			list1.append('n')
		if string3 == 't':
			list1.append('w')
		if string3 == 'u':
			list1.append('j')
		if string3 == 'v':
			list1.append('p')
		if string3 == 'w':
			list1.append('f')
		if string3 == 'x':
			list1.append('m')
		if string3 == 'y':
			list1.append('a')
		if string3 == 'z':
			list1.append('q')
	string2 = ''.join(list1)
	if case != 30:
		out.write("Case #%d: %s\n" % (case, string2)) 
	if case == 30:	
		out.write("Case #%d: %s" % (case, string2))
	case += 1


















