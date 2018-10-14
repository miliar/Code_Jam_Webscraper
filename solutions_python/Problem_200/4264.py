

def isTidy(n): 
	lastDigit = n % 10
	tmp = n / 10

	while ( tmp > 0 ):
		currentDigit = tmp % 10
		if currentDigit > lastDigit:
			return False
		tmp = tmp / 10
		lastDigit = currentDigit

	return True

def findLastTidy(num):
	if (isTidy(num)):
		return num
	else:
		strNum = str(num)
		lastNum = strNum[0]
		for idx, digit in enumerate(strNum[1:]):
			x = int(digit)
			y = int(lastNum)

			if x == y or y > x:
				sub = int(strNum[idx+1:]) + 1
				return num - sub
			lastNum = digit



inFile = open("/home/vic/Downloads/B-small-attempt0.in").readlines()[1:]
for i, f in enumerate(inFile):
	file = open("out", "a+")
	out = "Case #%d: %d\n"%(i+1, findLastTidy(int(f)))
	file.write(out)
	file.close()
