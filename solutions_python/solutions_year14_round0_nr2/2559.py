# Tashiv Sewpersad
# Google Code Jam 2014
# Qualiification Round - Question 2

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
	CookieRate = 2
	FactoryCost,Factorygain,WinTarget = getLine().split()
	FactoryCost = eval(FactoryCost)
	Factorygain = eval(Factorygain)
	WinTarget = eval(WinTarget)
	BestTime = WinTarget / CookieRate
	advTime = FactoryCost / CookieRate
	CookieRate += Factorygain
	NewTime = advTime + (WinTarget / CookieRate)
	while NewTime <= BestTime:
		BestTime = NewTime
		advTime += (FactoryCost / CookieRate)
		CookieRate += Factorygain
		NewTime = advTime + (WinTarget / CookieRate)
	BestTime = round(BestTime,7)
	sFormat = "{0:.7f}"
	sOutput += "Case #" + str(i) + ": " + sFormat.format(BestTime) + "\n"
writeOutput(sOutput)

## Final Code
TFile.close()  	
	 
	


