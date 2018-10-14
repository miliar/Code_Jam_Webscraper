def tictac(myfile):
	f = open(myfile, "r")
	g = open("file5.out", "w")
	numExamples = int(float(f.readline()))
	k = 1
	while (k < numExamples+1):
		lines = []
		#parse next 4 lines
		i = 0
		while i < 4:
			if k != numExamples:
				line = list(f.readline())[0:-1]
			else:
				line = list(f.readline())
			print("check rows---------------")
			print(line)
			lines.append(line)
			print(lines)
			print("\n")
			#check row
			if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
				g.write("Case #" + str(k) + ": " + "X won\n")
				i = 0
				lines = []
				for q in range(i,4):
					f.readline()
				k += 1
				continue
			elif line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
				g.write("Case #" + str(k) + ": " + "O won\n")
				i = 0
				lines = []
				for q in range(i,4):
					f.readline()
				k += 1
				continue
			elif i == 3:
				#check columns
				print("check columns---------------")
				j = 0
				while j < 4:
					column = []
					column.append(lines[0][j])
					column.append(lines[1][j])
					column.append(lines[2][j])
					column.append(lines[3][j])
					print(column)
					if column.count('X') == 4 or (column.count('X') == 3 and column.count('T') == 1):
						g.write("Case #" + str(k) + ": " + "X won\n")
						break
					elif column.count('O') == 4 or (column.count('O') == 3 and column.count('T') == 1):
						g.write("Case #" + str(k) + ": " + "O won\n")
						break
					elif j == 3:
						# check diagonals
						print("check diagonals---------------")
						d = 0
						while d < 2:
							diagonal = []
							diagonal.append(lines[0][d*3])
							diagonal.append(lines[1][1+(d*1)])
							diagonal.append(lines[2][2+(d*(-1))])
							diagonal.append(lines[3][3+(d*(-3))])
							print(diagonal)
							if diagonal.count('X') == 4 or (diagonal.count('X') == 3 and diagonal.count('T') == 1):
								g.write("Case #" + str(k) + ": " + "X won\n")
								break
							elif diagonal.count('O') == 4 or (diagonal.count('O') == 3 and diagonal.count('T') == 1):
								g.write("Case #" + str(k) + ": " + "O won\n")
								break
							elif d == 1:
								#check if draw or game is not over yet
								print("check draw/game over yet---------------")
								t = 0
								while t < 4:
									print(t)
									print(lines[t])
									if '.' in lines[t]:
										print("BOOOO")
										g.write("Case #" + str(k) + ": " + "Game has not completed\n")
										break
									elif t == 3:
										g.write("Case #" + str(k) + ": " + "Draw\n")
										break
									else:
										t += 1
							d += 1
					j += 1
			i += 1
		k += 1
		f.readline()
	f.close()
	g.close()

print tictac('A-small-attempt0.in')
