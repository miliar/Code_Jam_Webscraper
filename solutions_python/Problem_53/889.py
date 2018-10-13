import fileinput
			
lines = open('inputfile2', 'r').readlines()
f = open('outputfilelarge', 'w')
n =	long(lines[0])
for x in range(1, n+1):
	linesplit = lines[x].split(" ")
	snappers = long(linesplit[0])
	snaps = long(linesplit[1])
#	print snappers
#	print snaps
	a = 2**snappers
	b = snaps + 1
#	print a
#	print b
	if b % a == 0:		
	 	f.write("Case #" + str(x) + ": ON\n")
	else:
		f.write("Case #" + str(x) + ": OFF\n")
