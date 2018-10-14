def main():
	file = open("A-large.in")
	with file as f:
		lines = f.readlines()
		loops = int(lines[0])
		for i in range(0, loops):
			j = (i * 5) + 1
			group = lines[j:j+4]
			check_solved(i+1, group)
	file.close()

def empty():
	return {"X":0, "T":0, ".": 0, "O":0}

def check_solved(i, matrix):
	m = []
	for j in range(0, 4):
		row = []
		for k in range(0,4):
			row.append(matrix[j][k])
		m.append(row)
	
	total = empty()
	total_d = empty()
	total_d2 = empty()

	for j in range(0, 4):
		total_x = empty()
		total_y = empty()
		for k in range(0, 4):
			if j == k:
				total_d[m[j][k]] = total_d[m[j][k]] + 1
			elif -j == k-3:
				total_d2[m[j][k]] = total_d2[m[j][k]] + 1
			
			total_x[m[j][k]] = total_x[m[j][k]] + 1
			total_y[m[k][j]] = total_y[m[k][j]] + 1
			total[m[j][k]] = total[m[j][k]] + 1
			
		if total_x["X"] + total_x["T"] == 4 or total_y["X"] + total_y["T"] == 4:
			message(i, "X won")
			return
		elif total_x["O"] + total_x["T"] == 4 or total_y["O"] + total_y["T"] == 4:
			message(i, "O won")
			return

	if total_d["X"] + total_d["T"] == 4 or total_d2["X"] + total_d2["T"] == 4:
		message(i, "X won")
		return
	elif total_d["O"] + total_d["T"] == 4 or total_d2["O"] + total_d2["T"] == 4:
		message(i, "O won")
		return
	elif total["."] < 1:
		message(i, "Draw")
		return
	else:
		message(i, "Game has not completed")
		return

def message(i, m):
	file = open('output', 'a')
	file.write("Case #%s: %s\n"%(i,m))
	file.close()
main()
