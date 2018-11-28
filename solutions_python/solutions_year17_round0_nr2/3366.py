def toDigitList(N):
	string = str(N)
	digitList = []

	for digit in string:
		digitList.append (int(digit))

	return digitList

def isTidy(N):
	return isTidyList(toDigitList(N))

def isTidyList(digits):
	if(len(digits)<2):
		return True
	elif(digits[0]<=digits[1]):
		return isTidyList(digits[1:])
	else:
		return False

def allTidy(N):
	tidyList = []
	for i in range(N):
		if(isTidy(i)):
			tidyList += [i]
	return tidyList



t = int(input())
L = allTidy(1000)
for i in range(1, t + 1):
    N = int(input())
    result = 0
    for j in range(len(L)):
    	if L[j]<=N:
    		result = L[j]
    print("Case #" + str(i) + ": " + str(result))
