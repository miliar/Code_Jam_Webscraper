from sys import stdin

data = stdin.readlines()
number = int(data[0])
final = [data[i:i+5] for i in xrange(1, len(data), 5)]

def checksquare(square):
	splitline, dia1, dia2 = [], [], []
	spl1, spl2, spl3, spl4 = list(square[0]), list(square[1]), list(square[2]), list(square[3])
	splitline.append(spl1)
	splitline.append(spl2)
	splitline.append(spl3)
	splitline.append(spl4)
	vert = zip(*splitline)
	dia1.append(splitline[0][0])
	dia1.append(splitline[1][1])
	dia1.append(splitline[2][2])
	dia1.append(splitline[3][3])
	dia2.append(splitline[0][3])
	dia2.append(splitline[1][2])
	dia2.append(splitline[2][1])
	dia2.append(splitline[3][0])
	xh, oh, xv, ov, xd1, od1, xd2, od2 = 0, 0, 0, 0, 0, 0, 0, 0
	drawcheck = False
	xth, oth, xtv, otv, xtd1, otd1, xtd2, otd2, = 0, 0, 0, 0, 0, 0, 0, 0

	for i in range(3):
		drawcheck = False
		if square[i].count('X') >= 3:
			if square[i][0] == square[i][1] == square[i][2] or square[i][1] == square[i][2] == square[i][3]:
				xh = square[i].count('X')
				if square[i].count('X') == 3 and square[i].count('T') == 1:
					xth = 1
		if square[i].count('O') >= 3:
			if square[i][0] == square[i][1] == square[i][2] or square[i][1] == square[i][2] == square[3]:
				oh = square[i].count('O')
				if square[i].count('O') == 3 and square[i].count('T') == 1:
					oth = 1
		if square[i].count('.') == 0:
			drawcheck = True


	for i in range(4):
		vert[i] = ''.join(vert[i])
	vert.pop()
	for j in range(3):
		if vert[j].count('X') >= 3:
			if vert[j][0] == vert[j][1] == vert[j][2] or vert[j][1] == vert[j][2] == vert[j][3]:
				xv = vert[j].count('X')
				if vert[j].count('X') == 3 and vert[j].count('T') == 1:
					xtv = 1
		if vert[j].count('O') >= 3:
			if vert[j][0] == vert[j][1] == vert[j][2] or vert[j][1] == vert[j][2] == vert[j][3]:
				ov = vert[j].count('O')
				if vert[j].count('O') == 3 and vert[j].count('T') == 1:
					otv = 1

	dia1 = ''.join(dia1)
	if dia1.count('X') >= 3:
		if dia1[0] == dia1[1] == dia1[2] or dia1[1] == dia1[2] == dia1[3]:
			xd1 = dia1.count('X')
			if dia1.count('X') == 3 and dia1.count('T') == 1:
				xtd1 = 1
	if dia1.count('O') >= 3:
		if dia1[0] == dia1[1] == dia1[2] or dia1[1] == dia1[2] == dia1[3]:
			od1 = dia1.count('O')
			if dia1.count('O') == 3 and dia1.count('T') == 1:
				otd1 = 1

	dia2 = ''.join(dia2)
	if dia2.count('X') >= 3:
		if dia2[0] == dia2[1] == dia2[2] or dia2[1] == dia2[2] == dia2[3]:
			xd2 = dia2.count('X')
			if dia2.count('X') == 3 and dia2.count('T') == 1:
				xtd2 = 1
	if dia2.count('O') >= 3:
		if dia2[0] == dia2[1] == dia2[2] or dia2[1] == dia2[2] == dia2[3]:
			od2 = dia2.count('O')
			if dia2.count('O') == 3 and dia2.count('T') == 1:
					otd2 = 1
	
	xwin = max(xh,xv,xd1,xd2)
	owin = max(oh,ov,od1,od2)

	if xwin > owin:
		if xwin == 4 and owin == 3 or xwin == 4 and owin == 0:
			return 1
		elif xwin == 3 and owin == 0:
			if xth == 1 or xtv == 1 or xtd1 == 1 or xtd2 == 1:
				return 1
			else:
				return 3
	elif owin > xwin:
		if owin == 4 and xwin == 3 or owin == 4 and xwin == 0:
			return 2
		elif owin == 3 and xwin == 0:
			if oth == 1 or otv == 1 or otd1 == 1 or otd2 == 1:
				return 2
			else:
				return 3
	elif owin == xwin:
		if xwin == 3 and owin == 3:
			if xth == 1 or xtv == 1 or xtd1 == 1 or xtd2 == 1:
				return 1
			elif oth == 1 or otv == 1 or otd1 == 1 or otd2 == 1:
				return 2
			elif drawcheck == True:
				return 3
			else:
				return 4
		elif xwin == 0 and owin == 0:
			if drawcheck == True:
				return 3
			else:
				return 4
	elif drawcheck == True:
		return 3
	else:
		return 4



	
open('out.txt', 'w').close()	
for i in range(number):
	result = checksquare(final[i])
	output = open("out.txt", "a")
	if result == 1:
		output.write('Case #' + str(i+1) +': X won\n')
	elif result == 2:
		output.write('Case #' + str(i+1) +': O won\n')
	elif result == 3:
		output.write('Case #' + str(i+1) +': Draw\n')
	else:
		output.write('Case #' + str(i+1) +': Game has not completed\n')
	output.close()



	



