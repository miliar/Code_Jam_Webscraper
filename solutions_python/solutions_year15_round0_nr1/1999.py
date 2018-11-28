#!/usr/bin/python
import sys

file_arg = sys.argv[1]
f = open(file_arg, 'r')
string = ""

for i in range(int(f.readline())):
	line = f.readline().split(' ')
	mc = int(line[0])
	a = line[1];

	s = 0
	need = 0
	for x in range(mc + 1):
		sc = int(a[x])
		
		if s <= x and sc == 0:
			need += 1
			s += 1
		else:
			s += sc
		print(x,s)

	string+="Case #" + str(i + 1) + ": " + str(need) + "\n"

print(string)
text_file = open("output.out", "w")
text_file.write(string)
text_file.close()