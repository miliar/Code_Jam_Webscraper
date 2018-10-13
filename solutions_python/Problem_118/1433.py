import math
f = open("in.txt")
#T = f.readlines
T = int(f.readline())

w = open("out.txt", "w")

def isPalyndrome(numberString):
	for i in range(len(numberString) / 2):
		if numberString[i] != numberString[len(numberString) - 1 - i]:
			return False
	return True

for i in range(T):
	line = f.readline().split()
	start = int(line[0])
	end = int(line[1])
	count = 0
	for j in range(start, end + 1):
		sqrt = math.sqrt(j)
		if(isPalyndrome(str(j)) and int(sqrt) * int(sqrt) == j and isPalyndrome(('%.0f' % sqrt))):
			count = count + 1
	w.write("Case #" + str(i + 1) + ": " + str(count) + "\n")
