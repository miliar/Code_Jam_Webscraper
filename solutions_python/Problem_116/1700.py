def file_read(file):
	file_open = open(file, 'r')
	
	for line in file_open:
		yield line
	
	file_open.close()
	
def analyse(arr):
	print arr
	empty = 0
	rows = [3,3,3,3]
	cols = [3,3,3,3]
	diag = [3,3]
	for i in xrange(0,4):
		for j in xrange(0,4):
			if arr[i][j] == 0:
				empty = 1
			rows[i] = rows[i]&arr[i][j]
			cols[j] = cols[j]&arr[i][j]
	
			if i == j:
				diag[0] = diag[0]&arr[i][j]
	
			if i + j == 3:
				diag[1] = diag[1]&arr[i][j]
	
	for i in xrange(0,4):
		if rows[i] > 0:
			if rows[i] == 1:
				return ": X won"
			else :
				return ": O won"
		if cols[i] > 0:
			if cols[i] == 1:
				return ": X won"
			else :
				return ": O won"
	
	for i in xrange(0,2):
		if diag[i] > 0:
			if diag[i] == 1:
				return ": X won"
			else :
				return ": O won"
				
	if empty == 0:
		return ": Draw"
		
	return ": Game has not completed"

input = file_read('A-large.in')
output = open("A-large.out","w")

N = int(input.next())

for i in xrange(N):
	arr = []
	for j in xrange(4):
		next_input = input.next()
		arr += [[]]
		for k in range(4):
			if next_input[k] == 'X':
				arr[j] += [1]
			elif next_input[k] == 'O':
				arr[j] += [2]
			elif next_input[k] == 'T':
				arr[j] += [3]
			else:
				arr[j] += [0]
	
	output.write("Case #"+str(i+1)+analyse(arr)+"\n")
	print "case #"+(str(i+1))
	if i < N-1:
		input.next()	

output.close()