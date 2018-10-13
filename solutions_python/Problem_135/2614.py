#!/usr/bin/python


import fileinput

def log(x):
	if 0:
		print x

# problem a

raw_file = list()
for line in fileinput.input():
	raw_file.append(line)


testcases = int(raw_file[0])
log("There are " + str(testcases) + " Testcases")
for n in range(testcases):
	log("=======================================================")
	log("Doing Testcase " + str(n) + ":")
	
	m_1 = range(4)
	m_2 = range(4)
	# read the rows
	row_1 = int(raw_file[1+n*10])
	row_2 = int(raw_file[6+n*10])
	log("row_1: "+str(row_1)+" row_2: " + str(row_2))
	
	# read the matrix
	m_1[0] = map(int,raw_file[2+n*10].split())
	m_1[1] = map(int,raw_file[3+n*10].split())
	m_1[2] = map(int,raw_file[4+n*10].split())
	m_1[3] = map(int,raw_file[5+n*10].split())
	log ("m1 r1: " + str(m_1[0]))
	log ("m1 r2: " + str(m_1[1]))
	log ("m1 r3: " + str(m_1[2]))
	log ("m1 r4: " + str(m_1[3]))
	m_2[0] = map(int,raw_file[7+n*10].split())
	m_2[1] = map(int,raw_file[8+n*10].split())
	m_2[2] = map(int,raw_file[9+n*10].split())
	m_2[3] = map(int,raw_file[10+n*10].split())
	log ("m2 r1: " + str(m_2[0]))
	log ("m2 r2: " + str(m_2[1]))
	log ("m2 r3: " + str(m_2[2]))
	log ("m2 r4: " + str(m_2[3]))

	same = set(m_1[row_1-1]) & set(m_2[row_2-1])
	#print "Set: " + str(same)
	if len(same) == 0:
		print "Case #"+str(n+1)+": Volunteer cheated!"
	elif len(same) == 1:
		print "Case #"+str(n+1)+": " + str(same.pop())
	else:
		print "Case #"+str(n+1)+": Bad magician!"
