# filename = "01-input-test"
filename = "01-A-small-attempt0"
fi = open(filename+'.in', 'r')
fo = open(filename+'.out', 'w')
lData = list()
debug = True
collect = ""
index = 0
strVal = 0

row1 = 0
cards1 = [] 
row2 = 0
cards2 = []
cases = []

for line in fi:
	if (index > 0):

		if (index % 10 == 1):
			row1 = int(line.strip())
		elif (index % 10 == 6):
			row2 = int(line.strip())
		elif (index % 10 > 1) and (index % 10 < 6):
			cards1.append(list(line.strip().split(' ')))
		elif (index % 10 == 0) or (index % 10 > 6):
			cards2.append(list(line.strip().split(' ')))

		if (index % 10 == 0):
			# print (row1, cards1)
			# print (row2, cards2)
			cases.append([(row1, cards1),(row2, cards2)])
			row1 = 0
			cards1 = [] 
			row2 = 0
			cards2 = []

	index = index + 1

# print cases

def check_input (case_number, input1, input2):
    output = "Case #" + str(case_number) + ": "
    new_set = set(input1[1][input1[0]-1]).intersection(set(input2[1][input2[0]-1]))
    
    #print "input1:", input1[1][input1[0]-1]
    #print "input2:", input2[1][input2[0]-1]
    
    if len(new_set) == 1:
        output += str(new_set.pop())
    elif len(new_set) > 1:
        output += "Bad magician!"
    else:
        output += "Volunteer Cheated!"
    
    return output

index = 1
solution = ""
for case in cases:
	solution = solution + check_input(index, case[0], case[1]) + '\n'
	index = index + 1

solution = solution.strip()
print solution
fo.write(solution)