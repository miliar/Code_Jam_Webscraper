import sys

def q1():
	f = open(sys.argv[1], 'r')
	solve(f)

def readArray(in_) :
	line = in_.readline()
	row_num = int(line)
	matrix = list()
	for j in range(4):
		line = in_.readline()
		matrix.append(line)
	split_ = matrix[row_num - 1].split(' ')
	first_set = set()
	for i in split_:
		first_set.add(int(i))
	#print first_set
	return first_set

def solve(inputFile):
	line = inputFile.readline()
	test_number = int(line)
	#print test_number
	for i in range(1, test_number  +1):
		set_1 = readArray(inputFile)
		set_2 = readArray(inputFile)
		set_inter = set_1.intersection(set_2)
		
		if len(set_inter) == 1 :
			for j in set_inter:
				print "Case #" + str(i) + ": "+ str(j)
		elif len(set_inter) == 0:
			print "Case #" + str(i) + ": Volunteer cheated!"
		else:
			print "Case #" + str(i) + ": Bad magician!"
		
		
q1()
		
		
			
			
		
	
		

