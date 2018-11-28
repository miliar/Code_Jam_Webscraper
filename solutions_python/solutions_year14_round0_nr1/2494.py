def findCommons(list1,list2):
	return set(list1) & set(list2)

def getOutput(row1,row2):

	common = findCommons(row1,row2)
	if (len(common)>1):
		return "Bad magician!"
	elif (len(common)==0):
		return "Volunteer cheated!"
	else:
		return common.pop()

def generateCase(file,case_no):
	row1=int(file.readline().split()[0])
	loop_counter=1
	while(loop_counter<row1):
		file.readline()
		loop_counter+=1
	row1_data=file.readline().split()
	while (loop_counter<4):
		file.readline() 
		loop_counter+=1

	row2=int(file.readline().split()[0])
	loop_counter=1
	while(loop_counter<row2):
		file.readline()
		loop_counter+=1
	row2_data=file.readline().split()
	while (loop_counter<4):
		file.readline()
		loop_counter+=1

	"""
	print "row 1 :"+str(row1)
	print "row 2 :"+str(row2)
	print "row 1 data:"
	print row1_data
	print "row 2 data:"
	print row2_data 
	print "common"	
	"""
	print "Case #"+str(case_no)+": "+str(getOutput(row1_data,row2_data))

file=open("A-small-attempt0.in","r")
number_of_cases=int(file.readline().split()[0])
loop_c=1
while (loop_c<=number_of_cases):
	generateCase(file,loop_c)
	loop_c+=1

file.close()
