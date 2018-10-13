def valid_spot(yard, x_, y_):
	val = int(yard[x_][y_])
	hor, vert = True, True
	for i in range(len(yard[x_])):
		if val < int(yard[x_][i]):
			#print "val:", val, "x:",x_,"y:",i,"yard[x][y]",yard[x_][i]
			hor = False
	for i in range(len(yard)):
		if val < int(yard[i][y_]):
			#print "2"
			vert = False
	return hor or vert

f = open("q2.in")
length = -1
for i in file("q2.in"):
	length+=1
num = int(f.next())
for problem in range(num):
	line = f.next().strip()
	index = line.find(" ")
	#print index,":", line
	x = int(line[:index])
	y = int(line[index+1:])
	#print x," ",y
	yard = []
	for i in range(x):
		line = f.next().strip()
		line = line.split()
		yard.insert(i, line)
	response = "YES"
	for x in range(len(yard)):
		for y in range(len(yard[x])):
			if not valid_spot(yard,x,y):
				response = "NO"

	print ("Case #%d:" % (problem+1)), response
