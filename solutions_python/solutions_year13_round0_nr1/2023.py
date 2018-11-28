import sys
import collections
def process(case,mat) :
	n = 4
	player = ""
	it = -1
	jt = -1
	end = True	
	for i in range(n) :
		for j in range(n) :
			if end and mat[i][j] == "." :
				end = False
			if mat[i][j] == "T" :
				it = i
				jt = j
	player = check(mat)	
	if player == "" :
		if it != -1 and jt != -1 :
			mat[it][jt] = "X"			
			player = check(mat)	
			if player == "" :
				mat[it][jt] = "O"
			player = check(mat)	
	if player != "" :
			msg = player+" won"
	else :
		if end :
			msg = "Draw"				
		else :
			msg = "Game has not completed"
	print "Case #{}: {}".format(case+1,msg)
def check(mat) :
	n = 4	
	player = ""
	l = True
	r = True	
	for i in range(n) :
		v = True
		h = True
		#vh
		for j in range(n) : 	
			if j == n-1 :
				continue	
			if mat[i][j] == "X" or mat[i][j] == "O" :
				if mat[i][j] != mat[i][j+1] :
					v = False
			else :
				v = False
			if mat[j][i] == "X" or mat[j][i] == "O" :
				if mat[j][i] != mat[j+1][i] :
					h = False
			else :
				h = False				
		if v :
			player = mat[i][0]
		elif h :
			player = mat[0][i]

		#lr
		if i == n-1 :
				continue

		if mat[i][i] == "X" or mat[i][i] == "O" :
			if mat[i][i] != mat[i+1][i+1] :
				l = False
		else :
			l = False
		if mat[i][n-i-1] == "X" or mat[i][n-i-1] == "O" :
			if mat[i][n-i-1] != mat[i+1][n-i-2] :
				r = False
		else :
			r = False
	if l :
		player = mat[0][0]
	elif r :
		player = mat[0][3]

	return player
# def lr(mat) :
# 	n = 4
# 	player = ""
# 	l = True
# 	r = True
# 	for i in range(n-1) :		
# 		if mat[i][i] == "X" or mat[i][i] == "O" :
# 			if mat[i][i] != mat[i+1][i+1] :
# 				l = False
# 		else :
# 			l = False
# 		if mat[i][n-i-1] == "X" or mat[i][n-i-1] == "O" :
# 			if mat[i][n-i-1] != mat[i+1][n-i-2] :
# 				r = False
# 		else :
# 			r = False
# 	if l :
# 		player = mat[0][0]
# 	elif r :
# 		player = mat[0][3]
# 	return player
f = open(sys.argv[1])
n = int(f.readline())
for i in range(n) :
	mat = []
	for k in range(4) :
		line = list(f.readline().replace("\n",""))
		mat.append(line)
	f.readline()
	# check(mat)
	process(i,mat)
