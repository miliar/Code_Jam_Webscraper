infile = raw_input("File: ")
lines = open(infile, 'r').readlines()
output = open(infile[:-3]+"_solution"+infile[-3:], "w")

T = lines.pop(0)
counter = 1
for line in lines:
	line = line.split()
	A = int(line[0])
	B = int(line[1])
	distinct = []
	total = 0
	for i in range(A, B+1):
		for s in range(1, len(str(i))):
			recycled = int(str(i)[s:]+str(i)[:s])
			if A <= i and i < recycled and recycled <= B and (i, recycled) not in distinct:
				distinct.append((i, recycled))
				total += 1
	output.write("Case #"+str(counter)+": "+str(total)+"\n")
	counter += 1
	
