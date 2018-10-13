from sys import stdin


def whoWin(lista):
	if(lista.count(".") > 0):
		return None
	if(lista[0] != "T"):
		who = lista[0]
	else:
		if(lista[1] != "T"):
			who = lista[1]
		else:
			if(lista[2] != "T"):
				who = lista[2]
			else:
				if(lista[3] != "T"):
					who = lista[3]
				else:
					return None
	comodin = "T"
	
	if((lista[1] == who or lista[1] == comodin) and (lista[2] == who or lista[2] == comodin) and (lista[3] == who or lista[3] == comodin)):
		return who

def getVertical(linea1, linea2, linea3, linea4):
	vertical1 = []
	vertical2 = []
	vertical3 = []
	vertical4 = []
	
	vertical1.append(linea1[0])
	vertical1.append(linea2[0])
	vertical1.append(linea3[0])
	vertical1.append(linea4[0])
	
	vertical2.append(linea1[1])
	vertical2.append(linea2[1])
	vertical2.append(linea3[1])
	vertical2.append(linea4[1])
	
	vertical3.append(linea1[2])
	vertical3.append(linea2[2])
	vertical3.append(linea3[2])
	vertical3.append(linea4[2])
	
	vertical4.append(linea1[3])
	vertical4.append(linea2[3])
	vertical4.append(linea3[3])
	vertical4.append(linea4[3])
	
	return vertical1, vertical2, vertical3, vertical4
	
def getDiagonal(linea1, linea2, linea3, linea4):
	diagonal1 = []
	diagonal2 = []
	
	diagonal1.append(linea1[0])
	diagonal1.append(linea2[1])
	diagonal1.append(linea3[2])
	diagonal1.append(linea4[3])
	
	diagonal2.append(linea1[3])
	diagonal2.append(linea2[2])
	diagonal2.append(linea3[1])
	diagonal2.append(linea4[0])
	
	return diagonal1, diagonal2

def completionGame(linea1, linea2, linea3, linea4):
	if(linea1.count(".") > 0):
		return False
	if(linea2.count(".") > 0):
		return False
	if(linea3.count(".") > 0):
		return False
	if(linea4.count(".") > 0):
		return False
	return True
	
def printWin(who):
	print who + " won"

def printDraw():
	print "Draw"

def printIncomplete():
	print "Game has not completed"


total = int(stdin.readline())
for it in range(total):
	print "Case #" + str(it+1) + ": ",
	
	stdin.readline()
	linea1 = stdin.readline()
	linea2 = stdin.readline()
	linea3 = stdin.readline()
	linea4 = stdin.readline()
	
	##Comprobar horizontales
	result = whoWin(linea1)
	if(result != None):
		printWin(result)
		continue
		
	result = whoWin(linea2)
	if(result != None):
		printWin(result)
		continue
		
	result = whoWin(linea3)
	if(result != None):
		printWin(result)
		continue
		
	result = whoWin(linea4)
	if(result != None):
		printWin(result)
		continue
	
	##Comprobar verticales
	verticales = getVertical(linea1, linea2, linea3, linea4)
	result = whoWin(verticales[0])
	if(result != None):
		printWin(result)
		continue
		
	result = whoWin(verticales[1])
	if(result != None):
		printWin(result)
		continue
		
	result = whoWin(verticales[2])
	if(result != None):
		printWin(result)
		continue
		
	result = whoWin(verticales[3])
	if(result != None):
		printWin(result)
		continue
	
	##Comprobar diagonales
	diagonales = getDiagonal(linea1, linea2, linea3, linea4)
	result = whoWin(diagonales[0])
	if(result != None):
		printWin(result)
		continue
		
	result = whoWin(diagonales[1])
	if(result != None):
		printWin(result)
		continue
		
	##Completion
	if(completionGame(linea1, linea2, linea3, linea4)):
		printDraw()
	else:
		printIncomplete()
