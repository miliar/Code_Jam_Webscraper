#!/bin/python
import sys

fileName = sys.argv[1]

inputFile = open(fileName, 'r')
outputFile = open(fileName.strip('.in')+'.out', 'w')

numOfTestCases = int(inputFile.readline().strip())
for i in xrange(numOfTestCases):
	line = inputFile.readline().strip()
	arr = line.split()
	index_arr = 0
	C = int(arr[index_arr])
	combinations = {}
	destructions = []
	for index_c in xrange(C):
		index_arr = index_arr + 1
		combinations[arr[index_arr][0:2]] = arr[index_arr][2]
		combinations[arr[index_arr][1] + arr[index_arr][0]] = arr[index_arr][2]
	index_arr = index_arr + 1
	D = int(arr[index_arr])
	for index_d in xrange(D):
		index_arr = index_arr + 1
		destructions.append(arr[index_arr][0:2])
		destructions.append(arr[index_arr][1] + arr[index_arr][0])
	index_arr = index_arr + 1
	N = int(arr[index_arr])
	elem_list = arr[index_arr + 1]
	final_list = []
	final_len = 0
	for elem in xrange(N):
		noChange = True
		if (final_len == 0):
			final_list.append(elem_list[elem])
			final_len = final_len + 1
			continue
		myStr = final_list[final_len-1] + elem_list[elem]
		if (combinations.has_key(myStr)):
			final_list.pop(final_len-1)
			final_list.append(combinations[myStr])
			noChange = False
		else:
			for index_final in xrange(final_len):
				myStr = final_list[index_final] + elem_list[elem]
				if (myStr in destructions):
					final_list = []				
					final_len = 0
					noChange = False
					break
		if noChange == True:
			final_list.append(elem_list[elem])
			final_len = final_len + 1
	resultStr = '[' + ', '.join(final_list) + ']'
	outputFile.write('Case #'+str(i+1)+': '+resultStr)
	if i != (numOfTestCases - 1):
		outputFile.write('\n')
inputFile.close()
outputFile.close()
