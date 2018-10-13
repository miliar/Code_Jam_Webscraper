def solver(N):
	for i in range(N):
		n = N - i


		if isTidy(n):
			return n
	return 0

def solver2(N):
	if isTidy(N):
		return N
	NStr = str(N)
	prev = -1

	if len(NStr) == 1:
		return True

	for idx in range(len(NStr)):
		iInt = int(NStr[idx])
		if prev == -1:
			prev = iInt
		else:
			if iInt < prev:
				temp = int(NStr[0:idx]) - 1
				if temp == 0:
					return fillNine(len(NStr)-idx)
				elif isTidy(temp):
					return str(temp) + fillNine(len(NStr)-idx)
				else:
					return solver2(temp) + fillNine(len(NStr)-idx)
			else:
				prev = iInt

def fillNine(len):
	sum = ''
	for i in range(len):
		sum = sum + '9'
	return sum

def isTidy(num):
	numStr = str(num)


	if len(numStr) == 1:
		return True

	prev = -1
	for a in reversed(numStr):
		if a == '0':
			return False
		aInt = int(a)
		if prev == -1:
			prev = aInt
		else:
			if aInt > prev:
				return False
			prev = aInt

	return True
# print(solver2(2329873))
# print(solver2(111111111110))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	data = input()
	number = int(data)
	print("Case #{}: {}".format(i, solver2(number)))