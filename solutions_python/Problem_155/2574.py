file = open('A-large.in', 'r')
results = open('results.txt', 'w')

number_cases = int(file.readline())

def number_zeros_gaps(list_in):
	total = 0
	flag = 0
	for i in range(0,len(list_in)):
		if(list_in[i] == 0):
			if(flag == 0):
				total += 1
			flag = 1
		else:
			flag = 0
	return total
	
def first_zero(list_in):
	for i in range(0,len(list_in)):
		if(list_in[i] == 0):
			return i
	return -1
	
def last_zero(list_in):
	for i in range(len(list_in)-1,-1,-1):
		if(list_in[i] == 0):
			return i
	return -1
			
for i in range(0,number_cases,1):

	sentence = file.readline()
	sentence = sentence.replace('\n','')
	sentence = sentence.split(' ')
	
	max_shyness = int(sentence[0])
	
	shyness_string = sentence[1]
	
	#
	shyness = []
	for a in range(0,max_shyness+1):
		shyness.append(int(shyness_string[a]))
	
	num_people = 0
	extra_needed = 0
	
	for a in range(0,len(shyness)):
		element = shyness[a]

		if element != 0:
			if num_people < a:
				extra_needed += (a-num_people)
				num_people += (a-num_people)
				
				num_people += element
			else:
				num_people += element
			
		#print("a: " + str(a) + "\tElement: " + str(element) + "\tNum_People: " + str(num_people) +
		#		"\tExtra Needed" + str(extra_needed))
	
	results.write("Case #" + str(i+1) + ": " +str(extra_needed) + "\n")
	print("Case #" + str(i+1) + ": " +str(extra_needed))