#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pprint import pprint

def solve(values):
	for item in values:
		print(item)
#print('Case #%(case)s: %(result)s'%{'case':case,'result':result})

if __name__ == '__main__':
	#src = open('A-small-attempt2.in','r')
	src = open('A-large.in','r')
	out = open('out.txt','w')

	case = int(src.readline())
	for cidx in range(0,int(case)):
		lines = [] 
		dia_a = []
		dia_b = []
		vline = [[],[],[],[]]
		for lidx in range(0,4):
			line = src.readline()
			row = list(line[:-1])
			dia_a.append(row[lidx])
			dia_b.append(row[3-lidx])
			lines.append(row)
			for vidx in range(0,4):
				vline[vidx].append(row[vidx])
		for line in vline:
			lines.append(line)
		lines.append(dia_a)
		lines.append(dia_b)

		pName = None
		for result in lines:
			if 'X' not in result and '.' not in result:
				pName = 'O'
			elif 'O' not in result and '.' not in result:
				pName = 'X'

		if pName is not None:
			result_src = "%s won"%pName
		else:
			isEnd = True
			for result in lines:
				if '.' in result:
					isEnd = False 

			if isEnd is True:
				result_src = 'Draw'
			else:
				result_src = 'Game has not completed'

		output_src = 'Case #%(cid)d: %(result)s\n'%{'cid':cidx+1,'result':result_src}
		out.write(output_src)
		print(output_src)

		line = src.readline()	

	src.close()
	out.close()
	#itemList = line[:-1].split('\t')
	#itemList = line[:-1].split(' ')
