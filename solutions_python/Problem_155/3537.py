def read_line_input(inp):
	max_shy = int(inp[0])
	if inp[-1] == '\n':
		val_s = inp[2:-1]
	else:
		val_s = inp[2:]

	val = list()
	for i in val_s:
		val.append(int(i))
	return max_shy,val

def execute(inp):

	max_shy = inp[0]
	vals  = inp[1]

	#print max_shy
	#print vals

	counter = 0
	shy_trigger = 0
	l = len(vals)

	for i in range(l):
		
		"""
		print "---- Step {} --- ".format(i)
		print "counter = {}".format(counter)
		print "shy trigger = {}".format(shy_trigger)
		"""
		
		if i == 0:
			if vals[i] == 0:
				counter+=1
				shy_trigger+=1
			else:
				shy_trigger += vals[i]

		else:
			if shy_trigger >= i:
				shy_trigger += vals[i]
			else:
				counter += i-shy_trigger
				shy_trigger += (i - shy_trigger) + vals[i]	
		
		"""	
		print "--- Post ---"
		print "counter = {}".format(counter)
		print "shy trigger = {} \n".format(shy_trigger)
		"""

		if shy_trigger >= max_shy:
			return counter	

file_inp = open('input.dat', 'r')
max_iter = int(file_inp.readline()[:-1])

file_out = open('output.dat','w')
case = 1

for line in file_inp:
	inp = read_line_input(line)
	#print "case #{}: {}".format(case,execute(inp))
	file_out.write("case #{}: {}".format(case,execute(inp)))
	print case
	if case < max_iter:
		file_out.write('\n')
	
	case+=1

file_out.close()

"""
line = f.readline()
inp = read_line_input(line)
print execute(inp)
"""

## --- test ---

"""

inp = [7,[0,2,0,1,0,0,3,1]]
print execute(inp)

"""