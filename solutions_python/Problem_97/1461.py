fin, fout = open("input.txt", "r"), open("output.txt", "w") 

def sp(s):
	spis = []
	for i in range(len(s)):
		spis += [s]
		s = s[1:] + s[0]
	return list(set(spis))
                           
for q in range(int(fin.readline())):
	l, r = map(int, fin.readline().split())
	num = 0
	for i in range(l, r+1):
		length = len(str(i))
		for t in sp(str(i)):
			if l <= i and i < int(t) and int(t) <= r and len(str(int(t))) == length:
				#print >> fout, "   " + str(num) + " " + str(i) + " - " + str(t)
				num += 1
	print >> fout, "Case #" + str(q+1) + ": " + str(num)
