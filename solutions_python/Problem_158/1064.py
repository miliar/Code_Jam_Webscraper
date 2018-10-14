OUTPATH = "out.txt"
WI = "RICHARD"
LO = "GABRIEL"
def loadCases (filePath):
	data = []
	nCases = 0
	with open (filePath, 'r') as file:
		fileData = file.read()
		data = fileData.split("\n")
		nCases = data.pop(0)
		data.pop()
	return (nCases, data)
	
def whowins (nCases, data):
	nCase = 0
	clearfile()
	while data:
		nCase += 1
		currentCase = data.pop(0)
		currentCase = currentCase.split(" ")
		X = int(currentCase[0])
		R = int(currentCase[1])
		C = int(currentCase[2])
		outp = ""
		if (R==1 or C==1) and X>2:
			outp = WI
		elif X > max(R,C):
			outp = WI
		elif (R==2 or C==2) and X > 3:
			outp = WI
		elif ((R*C)%X) > 0:
			outp = WI
		else:
			outp = LO
		writeOutput(nCase, outp)

def clearfile ():
	with open (OUTPATH, 'w') as file:
			file.write("")
		
def writeOutput (nCase, friendsNeed):
	with open (OUTPATH, 'a') as file:
		file.write ("Case #%i: %s\n" % (nCase, friendsNeed) )
		
if __name__ == "__main__":
	nCases, data =loadCases("D-small-attempt1.in")
	whowins (nCases, data)