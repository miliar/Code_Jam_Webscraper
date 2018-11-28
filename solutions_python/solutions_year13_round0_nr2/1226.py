#!/usr/bin/python

cases = raw_input()
for case in range(int(cases)):
	line = raw_input().split(" ")
	l = int(line[0])
	c = int(line[1])
	
	strfield = []
	for x in range(l):
		strfield.append(raw_input())

	field = []
	for line in strfield:
		fieldline = []
		for height in line.split(" "):
			fieldline.append(int(height))
		field.append(fieldline)

	no = False
	for y in range(l):
		for x in range(c):
			hBlock = False
			vBlock = False

			for i in range(l):
				if (field[y][x] < field[i][x]):
					vBlock = True
					break
			
			for j in range(c):
				if (field[y][x] < field[y][j]):
					hBlock = True
					break
				
			if hBlock and vBlock:
				no = True
				break

		if no:
			break
		
	if no:
		print "Case #"+str(case+1)+": NO"
	else:
		print "Case #"+str(case+1)+": YES"
