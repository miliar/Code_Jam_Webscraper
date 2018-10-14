def isTidy(l):
	for i in range(1, len(l)):
		if l[i] >= l[i - 1]:
			continue
		else:
			return False
	return True

def findMaxTidy(num):
	s = str(num)
	l = list(s)
	for i in range(len(l)):
		l[i] = int(l[i])
	while not isTidy(l):
		for i in range(1, len(l)):
			if l[-i] < l[-(i + 1)]:
				l[-(i + 1)] -= 1
				for j in range(1, i + 1):
						l[-j] = 9
	for i in range(len(l)):
		l[i] = str(l[i])
	l =''.join(l)
	l = int(l)
	return str(l)
	





infile = open("input_file.txt", 'r')
outfile = open("output_file.txt", 'w')


T = int(infile.readline())
for i in range(T):
	inStr = infile.readline().split()
	num = int(inStr[0])
	outfile.write("Case #" + str(i + 1) + ": " + findMaxTidy(num) + "\n")