import sys

line = sys.stdin.readline()
t = int(line)
cont = 0
while cont < t:
	line = sys.stdin.readline().split()
	smax =  int(line[0])
	w = line[1]

	i = 0
	f = 0
	tmpP = int(w[i])
	tmpA = 0
	i += 1
	while i <= smax:
		tmpA = 0
		num = int(w[i])
		if tmpP < i:
			tmpA = i - tmpP
		f += tmpA
		tmpP += tmpA + num
		i += 1
	cont += 1
	print "Case #%d: %d" % (cont, f)

