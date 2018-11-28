def tidyFast(n):
	if isTidy(n):
		return n
	else:
		digitList = []
		for i in str(n):
			digitList.append(int(i))
		firstNotTidy = 0
		for i in range(len(digitList)-1):
			if digitList[i] > digitList[i+1]:
				firstNotTidy = i
		digitList[firstNotTidy] = digitList[firstNotTidy] - 1
		for i in range(firstNotTidy + 1, len(digitList)):
			digitList[i] = 9
		n_string = ""
		for i in digitList:
			n_string += str(i)
		return tidyFast(int(n_string))

def isTidy(n):
	for i in range(len(str(n)) - 1):
		if int(str(n)[i]) > int(str(n)[i+1]):
			return False
	return True

t = int(input())
for i in range(1, t+1):
	print("Case #{}: {}".format(i, tidyFast(int(input()))))