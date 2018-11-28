import math
import random


def solve(s):
	s = list(s)
	digits = []

	a = s.count("G")
	for i in range(0, a):
		digits.append(8)
		for char in "EIGHT":
			s.remove(char)

	a = s.count("X")
	for i in range(0, a):
		digits.append(6)
		for char in "SIX":
			s.remove(char)

	while len(s):
		if "T" in s and "H" in s and "R" in s and s.count("E") >= 2:
			digits.append(3)
			for char in "THREE":
				s.remove(char)
			continue
		if "S" in s and "V" in s and "N" in s and s.count("E") >= 2:
			digits.append(7)
			for char in "SEVEN":
				s.remove(char)
			continue
		if "Z" in s and "E" in s and "R" in s and "O" in s:
			digits.append(0)
			for char in "ZERO":
				s.remove(char)
			continue
		if "F" in s and "O" in s and "U" in s and "R" in s:
			digits.append(4)
			for char in "FOUR":
				s.remove(char)
			continue
		if "F" in s and "I" in s and "V" in s and "E" in s:
			digits.append(5)
			for char in "FIVE":
				s.remove(char)
			continue
		if "I" in s and "E" in s and s.count("N") >= 2:
			digits.append(9)
			for char in "NINE":
				s.remove(char)
			continue
		if "O" in s and "E" in s and "N" in s:
			digits.append(1)
			for char in "ONE":
				s.remove(char)
			continue
		if "T" in s and "W" in s and "O" in s:
			digits.append(2)
			for char in "TWO":
				s.remove(char)
			continue

	digits.sort()
	digits = map(str, digits)
	return digits



name = "A-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")[0]
	#line = map(int, line)

	result = "".join(solve(line))
	fout.write("Case #" + str(i + 1) + ": " + result + "\n")
	print "Case #" + str(i + 1) + ": " + result

fi.close()
fout.close()