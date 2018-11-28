import sys


cases = int(sys.stdin.readline())
#print ("Cases: ")
#print (cases)
lines = [[0 for x in xrange(4)] for x in xrange(4)] 
win = False
f = open('output', 'w')

def analyzeGame(lines, i):
	global f
	global win
	if lines:
		for j in range(0,4):
			if lines[j].count('X') == 4  or (lines[j].count('X') == 3 and lines[j].count('T') == 1):
				#print("X won")
				f.write("X won\n")
				win = True
				return
			elif lines[j].count('O') == 4  or (lines[j].count('O') == 3 and lines[j].count('T') == 1):
				#print("O won")	
				f.write("O won\n")
				win = True
				return
		
	return 

def boardIsFull(lines):
	Ocount = 0
	Tcount = 0
	Xcount = 0
	for j in range(0,4):
		Ocount = Ocount + lines[j].count('O')
		Xcount = Xcount + lines[j].count('X')
		Tcount = Tcount + lines[j].count('T')
	if Ocount + Tcount + Xcount == 16:
		return True
	
def analyzeDiagonal(lines):
	global win
	global f
	if lines:
		aux = list()
		for j in range(0,4):
			aux.append(lines[j][j])	
		if aux.count('X') == 4  or (aux.count('X') == 3 and aux.count('T') == 1):
			#print("X won")
			f.write("X won\n")
			win = True
			return
		if aux.count('O') == 4  or (aux.count('O') == 3 and aux.count('T') == 1):
			#print("O won")
			f.write("O won\n")
			win = True
			return
		aux = list()
		aux.append(lines[0][3])
		aux.append(lines[1][2])
		aux.append(lines[2][1])
		aux.append(lines[3][0])
		if aux.count('X') == 4  or (aux.count('X') == 3 and aux.count('T') == 1):
			#print("X won")
			f.write("X won\n")
			win = True
			return
		if aux.count('O') == 4  or (aux.count('O') == 3 and aux.count('T') == 1):
			#print("O won")
			f.write("O won\n")
			win = True
			return
	
def transpose(lines):
	out = [[0 for x in xrange(4)] for x in xrange(4)] 
	aux = [0 for x in xrange(4)]
	if lines:
		for i in range(0,4):
			for j in range(0,4):
				aux[j] = lines[j][i]
			out[i] = list(aux)
	return out
	
j=0
for i in range(0,cases*5+1):
	if i%5 == 0:
		if i != 0:
			#print ("Case #"),
			#sys.stdout.write(':'),
			#sys.stdout.write(' ')
			#sys.stdout.write(str(i/5)),
			
			f.write("Case #")
			f.write(str(i/5)),
			f.write(':'),
			f.write(' '),
			
			analyzeGame(lines, i//5 - 1)
			if win == False:
				transposed = transpose(lines)
			if win == False:
				analyzeGame(transposed, i//5 - 1)
			if win == False:
				analyzeDiagonal(transposed);
			if win == False:
				if boardIsFull(lines):
					#sys.stdout.write("Draw\n")
					f.write("Draw\n")
				else:
					#sys.stdout.write("Game has not completed\n")
					f.write("Game has not completed\n")
			sys.stdin.readline()
		j=0
		win = False
		lines = {}
	else:
		read = sys.stdin.readline()
		lines[j] = list(read)
		#print lines
		#print j
		#print(lines[i//5][j])
		j = j+1
	

	
	
	
