inputfile = open('D-small-attempt9.in')
outputfile = open('d.out','w')
T = inputfile.readline()
for x in range(int(T)):
	data = inputfile.readline()
	data = data.split()
	X = int(data[0])
	R = int(data[1])
	C = int(data[2])
	win = 0
	if(X,R,C) == (3,1,3) or (X,R,C) == (3,3,1) or (X,R,C) == (4,2,4) or (X,R,C) == (4,4,2):
		win = 1

	if X == 4:
		if R == 2 and C == 2:
			win = 1
		if R ==1 and C == 4:
			win = 1
		if R ==4 and C == 1:
			print x+1,(X,R,C)
			win = 1

	if (R*C)%X != 0:
		win = 1

	if win == 0:
		#print "Case #"+str(x+1)+": GABRIEL\n"
		outputfile.write("Case #"+str(x+1)+": GABRIEL\n")
	else:
		#print "Case #"+str(x+1)+": RICHARD\n"
		outputfile.write("Case #"+str(x+1)+": RICHARD\n")
	
inputfile.close()
outputfile.close()