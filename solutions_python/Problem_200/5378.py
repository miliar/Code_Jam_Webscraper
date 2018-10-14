import sys

def isNonDescending(num):
	sNum = str(num)
	for i in range(len(str(sNum)) - 1):
		if int(sNum[i]) > int(sNum[i+1]):
			return False
	return True

cases = int(sys.stdin.readline())
for i in range(1, cases+1):
	n = int(sys.stdin.readline())
	num = n

	while not isNonDescending(num):
		num -= 1

	print("Case #{}: {}".format(i, num))
