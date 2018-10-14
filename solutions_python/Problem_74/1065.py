import math
from decimal import Decimal


#infile = open("B-large.in","r")
#infile = open("input.txt","r")
infile = open("A-small-attempt0.in","r")
firstr = 0
case = 1
records = infile.readlines()
infile.close()

instructions = []
B_inst = []
O_inst = []

i = 0
while i < len(records):
	#print records[i]
	if i == 0:
		i = i + 1
		continue
	records[i] = records[i].replace("\n","")
	rec = records[i].split(" ")
	n_inst = int(rec[0])  # number of instructions
	instructions = []
	B_inst = []
	O_inst = []
	cur_list = []
	next = 1
	if n_inst != 0:
		for k in range(next,len(rec)):
			robot = rec[k]
			if robot == "O":
				curlist = O_inst
				incur = "O"
			else:
				if robot == "B":
					curlist = B_inst
					incur = "B"
				else:
					curlist.append(int(robot))
					if incur == "O":
						O_inst = curlist
					else:
						B_inst = curlist
					instructions.append(incur+robot)
						
	time = 0
	
	next_inst = 0
	currentO = 1
	currentB = 1
	nextO = 0
	nextB = 0
	

	while next_inst < len(instructions):
		#print instructions[next_inst] + " " + str(next_inst)
		#var = raw_input("Enter something: ")
		curinst = "O"+str(currentO)
		if curinst == instructions[next_inst]: # push button
			nextO = nextO + 1  # next instruction in list
			next_inst = next_inst + 1  # go ahead with next inst BUT, check if we can do some with B
			if nextB < len(B_inst):
				if B_inst[nextB] > currentB:
					currentB = currentB + 1
				else:
					if B_inst[nextB] < currentB:
						currentB = currentB - 1
		else:
			curinst = "B"+str(currentB)
			if curinst == instructions[next_inst]: # push button
				nextB = nextB + 1  # next instruction in list
				next_inst = next_inst + 1  # go ahead with next inst BUT, check if we can do some with O
				if nextO < len(O_inst):
					if O_inst[nextO] > currentO:
						currentO = currentO + 1
					else:
						if O_inst[nextO] < currentO:
							currentO = currentO - 1
			else:
				if nextB < len(B_inst):
					if B_inst[nextB] > currentB:
						currentB = currentB + 1
					else:
						if B_inst[nextB] < currentB:
							currentB = currentB - 1
						
				if nextO < len(O_inst):
					if O_inst[nextO] > currentO:
						currentO = currentO + 1
					else:
						if O_inst[nextO] < currentO:
							currentO = currentO - 1
				
		time = time + 1
	
	
	print "Case #"+ str(case)+": "+str(time)
	case = case + 1
	i = i + 1
	
		
