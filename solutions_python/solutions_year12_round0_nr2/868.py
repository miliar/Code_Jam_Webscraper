'''
If a total score is t then the maximum possible score is:
	floor((t-2)/3)+2		*surprise
	floor((t-1)/3)+1		*not surprised

For each score
	check if the not surprised is at least p, if so +1
	else if surprised still available check if surprised score is at least p, if so +1 (and -1 surprise availability)
	else nothing
'''

###########################################################
# function defs
###########################################################


###########################################################
# input
###########################################################

input_file = 'B-large.in.txt'
input_data = open(input_file,'r').readlines()

###########################################################
# cases
###########################################################

output = ''
num_cases = int(input_data[0])
i = 1
for n in range(num_cases):
	line = input_data[i].rstrip().split()
	i+=1
	num_googlers = int(line[0])
	num_surprise = int(line[1])
	p = int(line[2])
	newline = []
	for l in line[3:]:
		newline.append(int(l))
	num_p=0

	for t in newline:
		if t < 2:
			if t == 0 and p == 0:
				num_p+=1
			elif t == 1 and p < 2:
				num_p+=1
		elif int((t-1.0)/3)+1 >= p:
			num_p+=1
		elif num_surprise > 0 and int((t-2.0)/3)+2 >= p:
			num_p+=1
			num_surprise-=1
	
	output += 'Case #%d: %d\n'%(n+1,num_p)

###########################################################
# output
###########################################################

outfile = open('output_large.txt','w')
outfile.write(output)
outfile.close()