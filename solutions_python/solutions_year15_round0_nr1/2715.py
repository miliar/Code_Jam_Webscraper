import sys

#Reding the number of test cases
no_test_cases = raw_input()

output = []
def min_persons(line):
	vals = line.split(" ")
	max = int(vals[0])
	audiences = list(vals[1])
	if max+1 == len(audiences):
		#do the processing
		stood_people = 0
		people_added = 0
		for i in range(len(audiences)):
			if int(audiences[i]) >0 and i > stood_people :
				#add people here
				people_added += i - stood_people
				stood_people = i
			stood_people += int(audiences[i])
				
		return str(people_added)
	else:
		return "Incorrect input for this case"
	count += 1
#Iterating throgh all the test cases

for i in range(1,int(no_test_cases)+1):
	line = raw_input()
        output.append("Case #"+str(i)+": "+min_persons(line))	

#printing output
for output_line in output:
	print output_line	






