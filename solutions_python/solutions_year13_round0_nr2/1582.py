#!/usr/bin/env python3

def getMin(dim, pattern):

	minData = {'val': 101, 'x': 0, 'y': 0}
	for y in range(dim[0]):
		for x in range(dim[1]):

			if minData['val'] > pattern[y][x]:
				minData['val'] = pattern[y][x]
				minData['x'] = x
				minData['y'] = y
	return minData

def emptyList(l):
	return not all(len(a) > 0 for a in l)

def checkPattern(case, dim, pattern):
	while not emptyList(pattern):
		# print(pattern)
		minData = getMin(dim, pattern)
		goodRow = True
		goodCol = True

		#column check
		for y in(range(dim[0])):
			if pattern[y][minData['x']] != minData['val']:
				goodCol = False
				break

		if goodCol:
			for y in(range(dim[0])):
				del pattern[y][minData['x']]
			dim[1] -= 1
			continue

		#row check
		for x in(range(dim[1])):
			if pattern[minData['y']][x] != minData['val']:
				goodRow = False
				break

		if goodRow:
			del pattern[minData['y']]
			dim[0] -= 1
			continue


		return 'NO'

	return 'YES'




if __name__ == "__main__":
	import sys
	filename = sys.argv[1]
	f = open(filename, "r")
	casesNum = int(f.readline())

	for case in range(casesNum):
		
		dim = list(f.readline().rstrip('\n').split(' '))
		dim[0] = int(dim[0])
		dim[1] = int(dim[1]) 
		pattern = list()

		for i in range(dim[0]):
			row = list(f.readline().rstrip('\n').split(' '))
			#to int
			row = [int(x) for x in row]
			pattern.append(row)
		print('Case #%d: %s' % (case+1, checkPattern(case, dim, pattern)))
		

