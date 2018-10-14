#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

bad_magician = "Bad magician!"
cheat = "Volunteer cheated!"

def readline(f):
	return f.readline()[:-1]

def run_program(in_file, out_file):
	cases = int(readline(in_file))
	print 'Cases: ', cases
	for i in range(0, cases):
		first_response = -1
		second_response = -1
		first_case = []
		second_case = []

		first_response = int(readline(in_file))
		for j in range(0, 4):
			first_case.append(readline(in_file).split(' '))
		second_response = int(readline(in_file))
		for j in range(0, 4):
			second_case.append(readline(in_file).split(' '))
		res = ''
		responses = set(first_case[first_response-1]).intersection(set(second_case[second_response-1]))
		if len(responses) > 1:
			res = bad_magician
		elif len(responses) == 0:
			res = cheat
		else:
			res = responses.pop()
		print first_response, first_case[first_response-1]
		print second_response, second_case[second_response-1]
		print 'Responses: ', responses
		print 'Case', (i+1), res
		out_file.write("Case #%d: %s\n" % (i+1, res))

if __name__ ==  "__main__":
	if len(sys.argv) == 3:
		f = open(sys.argv[1], 'r')
		o = open(sys.argv[2], 'w')
		run_program(f, o)
		f.close()
		o.close()
	else:
		print u"Número de parámetros incorrecto. Se esperan 2."
		print str(sys.argv)

