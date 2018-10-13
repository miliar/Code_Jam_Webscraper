def isTidy(num):
	s = str(num)
	l = list(s)
	for i in range(1, len(l)):
		if int(l[i]) >= int(l[i - 1]):
			continue
		else:
			return False
	return True

def findMaxTidy(num):
	x = num
	while x > 0:
		if isTidy(x):
			return str(x)
		else:
			x -= 1




infile = open("input_file.txt", 'r')
outfile = open("output_file.txt", 'w')


T = int(infile.readline())
for i in range(T):
	inStr = infile.readline().split()
	num = int(inStr[0])
	outfile.write("Case #" + str(i + 1) + ": " + findMaxTidy(num) + "\n")