import sys
import math

file = open(sys.argv[1])
T = int(file.readline())
#T=int(input())
for X in range(1,T+1):
	line = file.readline()
	number1= int(line.split(" ")[0])
	number2= int(line.split(" ")[1])
	sqrt1 = int(math.ceil(math.sqrt(number1)))
	sqrt2 = int(math.floor(math.sqrt(number2)))
	count = 0
	for num in range(sqrt1,sqrt2+1):
		strNum = str(num)
		if strNum == strNum[::-1]:
			strSqr = str(int(math.pow(num,2)))
			if strSqr == strSqr[::-1]:
				count = count + 1
	print("Case #"+str(X)+": "+str(count))

