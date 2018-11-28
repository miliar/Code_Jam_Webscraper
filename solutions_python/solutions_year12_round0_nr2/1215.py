#!/usr/bin/python
#coding=utf-8
import sys

norm_dict = {}
surp_dict = {}

def calculate(googlers, surprising, p, scores):
	normal_highscore = []
	surp_highscore = []
	for s in scores:
		normal_highscore.append(s/3 if s%3 == 0 else s/3+1)
		if s == 0:
			surp_highscore.append(0)
		else:
			surp_highscore.append(s/3 + 1 if s%3 < 2 else s/3+2)
	
	result = [1 if s >= p else 0 for s in normal_highscore]
	if surprising > 0:
		for i in range (0, len(result)):
			if result[i] == 0 and surp_highscore[i] >= p:
				result[i] = 1
				surprising -= 1
				if surprising == 0:
					break
	return sum(result)
	

if len(sys.argv) < 3:
	print "Uso: %s <input filename> <output filename>" % sys.argv[0]
	sys.exit()
input_filename = sys.argv[1]
output_filename = sys.argv[2]
file = open(input_filename, "r")
output_file = open(output_filename, "w")
cases = int(file.readline())

for case in range(0,cases):
	whole_line = file.readline().split()
	googlers = int(whole_line[0])
	surprising = int(whole_line[1])
	p = int(whole_line[2])
	scores = [int(sc) for sc in whole_line[3:]]
	result = calculate(googlers, surprising, p, scores)
	output_file.write('Case #%d: %d\n' % (case+1, result))

file.close()
output_file.close()

