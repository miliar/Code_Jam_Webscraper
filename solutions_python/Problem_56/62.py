fileName = 'A-large.in'

f = open(fileName,'r');
fOut = open(fileName + '-solution.txt','w')

nrOfCases = int(f.readline()) #nr test cases is ignored

def remove_values_from_list(the_list, val):
	while val in the_list:
		the_list.remove(val)


def tryDiff(char, col, row, x, y, lists, cnt):
	newCol = col+x
	newRow = row+y
	if(len(lists) < newCol + 1 or len(lists[newCol]) < newRow + 1 or newCol < 0 or newRow < 0):
		return False
	#print 'Cnt: ' + str(cnt) + 'newCol: ' + str(newCol) + ', newRow: ' + str(newRow)
	
	match = (lists[newCol][newRow] == char)

	if(cnt > 2 and match):
		return tryDiff(char, newCol, newRow, x, y, lists, cnt-1)
	#if(match == True):
	#	print 'found true row at ' + str(newCol) + ', ' + str(newRow)
	#	print 'vals: ' + str(lists[newCol][newRow]) + ' and ' + char
	return match

for case in range (0, nrOfCases):
	
	result = ''
	
	#read the line(s)
	line = f.readline()
	#print line
	N = int(line.split(" ")[0])
	K = int(line.split(" ")[1])
	
	lists = []
	
	for linecnt in range(0, N):
		reversedline = []
		readline = f.readline()[0:-1]
		for char in readline:
			reversedline.append(char)
		reversedline.reverse()
		lists.append(reversedline)
	
	for column in lists:
		remove_values_from_list(column, '.')

	Rcomplete = False
	Bcomplete = False
		
	#for column in lists:
	#	print column	
	
	for col in range(0,len(lists)):
		for row in range(0,len(lists[col])):
			#print 'startval (' +str(col) +',' + str(row)+ '): ' + lists[col][row]
			
			char = lists[col][row]
			
			if(char == 'R' and Rcomplete or char == 'B' and Bcomplete):
				continue
			
			if(tryDiff(char, col, row, 0,1, lists, K)):
				if(char == 'R'):
					Rcomplete = True
				else:
					Bcomplete = True
			if(tryDiff(char, col, row, 1,1, lists, K)):
				if(char == 'R'):
					Rcomplete = True
				else:
					Bcomplete = True
			if(tryDiff(char, col, row, -1,1, lists, K)):
				if(char == 'R'):
					Rcomplete = True
				else:
					Bcomplete = True
			if(tryDiff(char, col, row, 1,-1, lists, K)):
				if(char == 'R'):
					Rcomplete = True
				else:
					Bcomplete = True
			if(tryDiff(char, col, row, 0,-1, lists, K)):
				if(char == 'R'):
					Rcomplete = True
				else:
					Bcomplete = True
			if(tryDiff(char, col, row, -1,-1, lists, K)):
				if(char == 'R'):
					Rcomplete = True
				else:
					Bcomplete = True
			if(tryDiff(char, col, row, -1,0, lists, K)):
				if(char == 'R'):
					Rcomplete = True
				else:
					Bcomplete = True
			if(tryDiff(char, col, row, 1,0, lists, K)):
				if(char == 'R'):
					#print 'setting from r'
					Rcomplete = True
				else:
					#print 'setting from b'
					Bcomplete = True
				
			
	#print Rcomplete
	#print Bcomplete
	
	if(Rcomplete and 
	Bcomplete == False):
		result = 'Red'
	if(Bcomplete and  Rcomplete == False):
		result = 'Blue'
	if(Rcomplete and Bcomplete):
		result = 'Both'
	if(Rcomplete == False and Bcomplete == False):
		result = 'Neither'
	

	print 'Case #' + str(case+1) + ': ' + result
	fOut.write('Case #' + str(case+1) + ': ' + result + '\n')
f.close()
fOut.close()