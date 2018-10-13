import codejamhelper as h
import numpy as np
import os
import psyco as p

p.full()

data = h.get_case_list(h.get_file())

solutions = []

cases = []
while(len(data)>0):
	size = data[0].split()
	count = size[0]
	data.pop(0)
	case = []
	for i in xrange(int(count)):
		chars = []
		for char in data[0]:
			chars.append(char)
		case.append(chars)
		data.pop(0)
	cases.append(case)

f_out = open(os.path.join(h.OUTPUT_DIR, h.OUTPUT_FILENAME), 'w')

casenr = 1

for case in cases:
	for line in xrange(len(case)):
		for column in xrange(len(case[line])):
			if column+1 < len(case[line]) and line+1 < len(case):
				if case[line][column] == '#' and case[line][column+1] == '#' and case[line+1][column] == '#' and case[line+1][column+1] == '#':
					case[line][column] = "/"
					case[line][column+1] = "\\"
					case[line+1][column] = "\\"
					case[line+1][column+1] = "/"
	transformed = True
	for line in xrange(len(case)):
		for column in xrange(len(case[line])):
			if case[line][column] == '#':
				transformed = False
	if(transformed == False):
		f_out.write("Case #%d:\nImpossible"%(casenr))
	else:
		f_out.write("Case #%d:"%(casenr))
		for line in xrange(len(case)):
			f_out.write("\n")
			for column in xrange(len(case[line])):
				f_out.write("%s"%(case[line][column]))
	if(casenr<len(cases)):
		f_out.write("\n")
	casenr += 1
