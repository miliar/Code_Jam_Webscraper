#!/usr/sin/python

def nval(s, n):

	sum = 0

	q = -1
	for pos in range(len(s)-n+1):
		
		cons = True
		for check in range(n):
			if s[pos+check] in "aeiou":
				cons = False
				break

		if not cons:
			continue

		sum += (pos-q) * (len(s)-n+1-pos)
		q = pos

	return sum

fin = open("A-small.in", "r")
fout = open("A-small.out", "w")

T = int(fin.readline())

for i in range(T):
	L = fin.readline().split()
	fout.write("Case #" + str(i+1) + ": " + str(nval(L[0], int(L[1]))) + "\n")

fin.close()
fout.close()