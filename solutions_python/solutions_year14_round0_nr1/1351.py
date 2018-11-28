#!/usr/bin/python

def readMatrix(lineId):
	rows = []
	for i in xrange(4):
		rows.append(map(int, raw_input().split()))
	return rows[lineId - 1]

T = int(raw_input())

for tc in xrange(1, T + 1):
	lineId = int(raw_input())
	row1 = readMatrix(lineId)
	lineId = int(raw_input())
	row2 = readMatrix(lineId)
	duplicates = filter(lambda x: x in row2, row1)
	print "Case #%d:" % tc,
	if len(duplicates) == 0:
		print "Volunteer cheated!"
	elif len(duplicates) > 1:
		print "Bad magician!"
	else:
		print duplicates[0]
