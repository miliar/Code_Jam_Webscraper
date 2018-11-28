import numpy as np

def processinput(filename):
    f = open(filename, 'r')
    cases = int(f.readline())
    
    output = []
    for i in range(cases):
        row_string = f.readline().split()[1]
        row = []
        for char in row_string:
        	row.append(int(char))
        output.append(row)
    
    f.close()
    
    return output

def determine(case):
	standing = 0
	invites = 0
	for i in range(len(case)):
		if i <= standing or case[i] == 0:
			standing += case[i]
		else:
			invites += i - standing
			standing += invites + case[i]

	return invites

def output(infile, outfile):
    f = open(outfile, 'w')
    
    counter = 0
    input = processinput(infile)
    for case in input:
        counter += 1
        f.write('Case #' + str(counter) + ': ' + str(determine(case)) + '\n')
        
    f.close()
 
#output('a-test.in', 'a-test.out')   
output('A-small-attempt0.in', 'A-small-attempt0.out')