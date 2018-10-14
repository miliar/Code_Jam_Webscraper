import sys

def isSolved( str ):
	return str.count('+') == len(str)
	
def swapCharacters( string, numToSwap, index ):
	retList = ''
	subStr = string[index:index+int(numToSwap)]
	for c in subStr:
		if c == '-':
			retList += '+'
		else:
			retList += '-'
	
	return retList

inputFile = open(sys.argv[1], "r") 
outputFile = open(sys.argv[2], "w") 
t = inputFile.readline()
for i in range(int(t)):

	'''
	print('=================================')
	'''
	
	numbers = inputFile.readline()
	answer = 'IMPOSSIBLE'
	s = numbers.split(" ")[0].strip()
	k = numbers.split(" ")[1].strip()
	
	if isSolved(s):
		answer = 0
	elif s.count('-') == len(s) and len(s) % int(k) == 0:
		answer = int(len(s) / int(k))
	else:
		slist = list(s)
		processedList = s
		count = 0
		index = 0
		while( index < len(s) and index + int(k) <= len(s) ):
			'''
			print('Begin Index' + str(index))
			print('Current Character' + processedList[index])
			'''
			if processedList[index] == '-':
				count += 1
				newcharacters = swapCharacters(processedList,k,index)
				'''
				print('New Characters' + newcharacters )
				'''
				processedList = processedList[:index] + newcharacters + processedList[index+int(k):]
				if processedList.find('-') != - 1:
					index = processedList.find('-')
				else:
					index += int(k)
			else:
				index += 1
			
			'''
			print('S'+str(slist))
			print('P'+str(list(processedList)))
			print('End Index' + str(index))
			'''
			
			if isSolved( processedList ) :
				answer = count
				break
		
		if isSolved( processedList ) :
			answer = count
		else:
			answer = 'IMPOSSIBLE'
		
	outputFile.write('Case #'+ str(i+1) + ': ' + str(answer) +'\n')

inputFile.close

