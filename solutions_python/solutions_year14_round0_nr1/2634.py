# Tashiv Sewpersad
# Google Code Jam 2014
# Qualiification Round - Question 1

## TFile Handeling
sInFile = "input.in"
sOutFile = "output.txt"
TFile = open(sInFile,"r")

## Declarations
def getLine():
	sResult = TFile.readline()
	sResult = sResult[0:len(sResult)-1]
	return sResult

def writeOutput(sOutput):
	OutFile = open(sOutFile,"w")
	OutFile.write(sOutput)
	OutFile.close()

## Live Code
sOutput = ""
iTcases = eval(getLine())
for i in range(1,iTcases+1):
	iAns1 = eval(getLine())
	iCards = []
	for j in range(0,4):
		iCards.append(getLine())
	iSelect1 = iCards[iAns1-1].split()
	iAns2 = eval(getLine())
	iCards = []
	for j in range(0,4):
		iCards.append(getLine())
	iSelect2 = iCards[iAns2-1].split()
	sCards = []
	for j in iSelect1:
		for k in iSelect2:
			if j == k:
				sCards.append(j)
	sOutput +=  "Case #" + str(i) + ": "
	if len(sCards) == 1:
		sCard = str(sCards)
		sOutput +=  sCard[2:len(sCard)-2]
	elif len(sCards) == 0:
		sOutput += "Volunteer cheated!"
	else:
		sOutput += "Bad magician!"
	sOutput += "\n"	
writeOutput(sOutput)

## Final Code
TFile.close()  	
	 
	


