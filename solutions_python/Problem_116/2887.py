tableHeight = 4
empty = '.'
play1 = 'X'
play2 = 'O'
wild = 'T'
inputfile = "input.txt"
outputfile = "output.txt"

completed = True
winner = ''
aux = ''

def setwinner(pos1,pos2):
	global aux
	global winner
	if(pos1 == 'T'):
		if(pos2 == aux):
			if (not pos2 in winner): winner += pos2
	else:
		if(pos1 == aux):
			if (not pos1 in winner): winner += pos1

	aux = ''

def check(a,b):
	global aux

	if((a==empty) | (b==empty)):
		global completed
		completed = False
	else:

		res = ((a == b) | (a == wild) | (b == wild))
		if(res and (aux!='') ):
			res = ((aux == a) | (aux == b))
			return res
		else:
			if(res):
				if(a==wild):
					aux = b
				else:
					aux = a
			return res
			


def checkrows(m):
	global aux
	for i in range(tableHeight):
		row = m[i]
		fin = len(row)-1
		for j in range(fin):

			
			pos1 = m[i][j]
			pos2 = m[i][j+1]


			if(check(pos1,pos2)):
				if(j+1==fin):
					setwinner(pos1,pos2)

			elif(not check(pos1,pos2)):
				break
		aux = ''

def checkcolums(m):
	global aux
	row = m[0]

	fin = len(row)
	for j in range(fin):

		for i in range(tableHeight-1):
			pos1 = m[i][j]
			pos2 = m[i+1][j]

			if(check(pos1,pos2)):
				if(i+1==tableHeight-1):
					setwinner(pos1,pos2)

			elif(not check(pos1,pos2)):
				break
		aux = ''

def checkdiagonal(m):
	global aux
	d1=[]
	d2=[]
	j=0
	for i in range(len(m[0])):
		row = m[i]
		fin = len(row)
		d1.append(m[i][j])
		d2.append(m[i][fin-1-j])
		j += 1

	
	fin = len(d1)-1
	for w in range (fin):
		pos11 = d1[w]
		pos12 = d1[w+1]
		
		if(check(pos11,pos12)):
			if(w+1==fin):
				setwinner(pos11,pos12)
		else:
			break
	aux = ''
	for w in range (fin):
		pos21 = d2[w]
		pos22 = d2[w+1]
		
		if(check(pos21,pos22)):
			if(w+1==fin):
				setwinner(pos21,pos22)

		else:
			break	
	aux = ''
				

def whowon(m):
	global winner
	winner = ''
	global completed
	completed = True

	checkrows(m)
	checkcolums(m)
	checkdiagonal(m)
	if(winner == ''):
		if(completed):
			return 'Draw'
		else:
			return 'Game has not completed'

	elif(len(winner)==2):
		return 'Draw'
	else:
		return winner + ' won'




def main(infile = "input.txt", outfile = "output.txt"):
#	try:
		f = open(infile, 'r')
		try:
			fw = open(outfile, 'w')
		except:
			fw = None
	
		n = int(f.readline())
		for i in range (n):
			matrix = []
			for x in range (tableHeight):
				line = f.readline()
				line = line[0:(len(line)-1)]
				while(list(line)==[]):
					line = f.readline()
					line = line[0:(len(line)-1)]

				matrix.append(list(line))
			answer = whowon(matrix)
			if fw:
				fw.write('Case #%d: ' % (i+1))
				fw.write(answer + '\n')


		if fw:
			fw.close()
#	except:



#if __name__ == "__main__":
main(inputfile,outputfile)