import sys

sys.stdin.readline()
numLine = 1

def printFace(pancake):
	if pancake == True:
		return '+'
	elif pancake == False:
		return '-'
	else:
		return 'E'

for line in sys.stdin:

	i = 0
	pancakes = []

	while line[i] != ' ':
		
		if line[i] == '+':
			pancakes.append(True)
		if line[i] == '-':
			pancakes.append(False)

		i += 1
	
	k = int(line[i+1:])	
	pos = 0
	moves = 0

#	if numLine == 24:
#		print 'k =', k
	
	while pancakes != [True]*len(pancakes):

#		if numLine == 24:
#			prtMe = [printFace(elem) for elem in pancakes]
#			print ''.join(prtMe)


		if pos + k  > len(pancakes):
			break
		
		if pancakes[pos] == False:
			pancakes[pos:pos+k] = [not elem for elem in pancakes[pos:pos+k]]		
			moves += 1
			

		pos += 1	

	
#	if numLine == 24:
#		prtMe = [printFace(elem) for elem in pancakes]
#		print ''.join(prtMe)

	output = 'Case #' + str(numLine) + ': '
	
	if pancakes == [True]*len(pancakes):
		output += str(moves)
	else: output += 'IMPOSSIBLE'

	print output

	numLine +=1
