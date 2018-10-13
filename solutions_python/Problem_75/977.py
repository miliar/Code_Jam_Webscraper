import re
filename = "B-large"
f = open(filename+".in")
num_testcases = int(f.readline())
lines = []
num_comb = [0]
comb = []
num_opp = [0]
opp = []
num_n = [0]
elements = None
answer = [""]
index = [0]

for line in f:
	lines.append(line[:-1])



def check_combinations(answer):
	##print "Answer : " + answer[0]
	toCheck = answer[0][len(answer[0])-2:]
	
	for combination in comb:
		##print"@check_combinations"
		##print toCheck
		##print combination[:2]
		##print combination[1]+combination[0]
		
		if(toCheck == combination[:2] or toCheck ==(combination[1]+combination[0]) ):
			#print "MATCHED: " + combination[:2]
			answer[0] = answer[0][:len(answer[0])-2] + str(combination[-1])
			##print "ANSWER: " + answer[0]
			#print answer
			return
	return
	
def check_opposites(answer):
	for opposite in opp:
		pattern = opposite[0]+".*"+opposite[1]
		pattern1 = opposite[1]+".*"+opposite[0]
		match = re.search(pattern,answer[0])
		if match:
			answer[0] = ""
			return
		match = re.search(pattern1,answer[0])
		if match:
			answer[0] = ""
			return
	return




for j in range(0, num_testcases):
	input = lines[j].split()
	
	num_comb[0] = int( input[0] )
	if( num_comb[0] > 0 ):
		for i in range (1,1+num_comb[0]):
			comb.append(input[i])
	
	num_opp[0] = int( input[1+num_comb[0]] )
	
	if( num_opp[0] > 0 ):
		for i in range ( 1 + num_comb[0] + 1 , num_comb[0]+2+num_opp[0]):
			opp.append(input[i])
	
	num_n[0] = int( input[ num_comb[0]+2+num_opp[0] ] )
	
	if( num_n[0] > 0 ):
			elements = "".join((input[num_comb[0]+3+num_opp[0]:]))
			
	#print i
	#print "num_comb: " + str(num_comb[0])
	#print "comb : " + str(comb)
	#print "num_opp : " + str(num_opp[0])
	#print "opp : " + str(opp)
	#print "num_n: " + str(num_n[0])
	#print "elements: " + str(elements)
	
	while(True):
		answer[0] = answer[0] + str( (elements[index[0]]))
		##print "i: " + str(index[0])
		#print "@while, answer= " + answer[0]
		index[0] = index[0] + 1 
		check_combinations(answer)
		check_opposites(answer)
		if( index[0] >= num_n[0] ):
			break
		
	toOutput = ", ".join(answer[0])
	toOutput = "[" + toOutput + "]"
	print "Case #"+str(j+1)+": "+toOutput
	num_comb = [0]
	comb = []
	num_opp = [0]
	opp = []
	num_n = [0]
	elements = None
	answer = [""]
	index = [0]
