#!/usr/bin/python
import sys

file_arg = sys.argv[1]
f = open(file_arg, 'r')
string = ""
for i in range(int(f.readline())):
	line = f.readline().split()

	cps = float(2)
	total = float(0)

	C = float(line[0])
	F = float(line[1])
	X = float(line[2])

	while X/cps > (X/(cps+F) + C/cps):
		total += C/cps
		cps += F
		
	total += X/cps

	string+="Case #" + str(i + 1) + ": " + str(total) + "\n"
print(string)
text_file = open("output.out", "w")
text_file.write(string)
text_file.close()