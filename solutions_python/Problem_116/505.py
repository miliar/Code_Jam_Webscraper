
import numpy as np

def readInput(filename):
	fid = open(filename, 'r')
	T = int(fid.readline())
	R = []
	
	for zzz in range(0,T):
		print '****************'
		M = np.zeros((4,4), dtype=np.int)
		for qqq in range(0,4):
			line = fid.readline().rstrip('\n')#.split()
			line = line.replace('.','0')
			line = line.replace('X','1')
			line = line.replace('O','2')
			line = line.replace('T','3')
			line = map(int,line)
			M[qqq] = line
		emptyline = fid.readline()		
		
		result = 'N'
		gameOpen = False

		lines = np.zeros((10,4), dtype=np.int)
		lines[0:4] = M
		lines[4:8] = M.transpose()
		lines[8] = M.diagonal()
		lines[9] = np.rot90(M).diagonal()

		for i in range(0,10):
			r = check_line(lines[i])
			if r == 1:
				result = 'X won'
				break
			elif r == 2:
				result = 'O won'
				break
			elif r == 3:
				gameOpen = True 
		
		if (result == 'N'):
			if gameOpen == True:
				result = 'Game has not completed'
			else:
				result = 'Draw'

		print result
		
		solution = result
		print "---"

		



		#when solution is obtained do 
		R.append(solution)
	
	print R
	fileOut = filename[0:-2] + 'out'
	writeSolution(R,fileOut)


def check_line(line):
	#check if the 4 element line contains a winning combination (4X,4O,3X1T,3O1T)
	#histogram of [. X O T]
	hist=np.zeros((4,1), dtype=np.int)
	for i in range(0,4):
		hist[line[i]] += 1

	#print hist[0]
	#print hist[1]
	#print hist[2]
	#print hist[3]
	#print "------"
	#analyze histogram
	if hist[0] > 0:	#if there is an empty cell -> no winner and game open
		return 3
	elif hist[1] == 4:
		return 1
	elif hist[2] == 4:
		return 2
	elif (hist[1] == 3) and (hist[3] == 1):
		return 1
	elif (hist[2] == 3) and (hist[3] == 1):
		return 2
	else:
		return 0

def writeSolution(R,filename):
	idx = 1
	fid = open(filename,'w')
	for line in R:
		h = 'Case #' + str(idx) + ': ' 
		hh = h + ''.join(str(line)) + '\n'
		fid.write(hh)
		idx += 1
	fid.close()



#D=readInput('sample')
#D=readInput('sample2')
#D=readInput('A-small-attempt0.in')
#D=readInput('A-small-practice.in')
D=readInput('A-large.in')


