inp=open('input1.txt').read().rsplit('\n')
count=inp[0]
owon="O won"
xwon="X won"
for index in range(0, int(count)):
	print "Case #%d: "%(index+1),
	mat=[]
	won=False
	for ln in range(index*5+1, index*5+5):
		row=[inp[ln][0],inp[ln][1],inp[ln][2],inp[ln][3]]
		row_x_count=row.count('X')
		row_o_count=row.count('O')
		if row_x_count+row.count("T")==4 and row_x_count>=3:
			print xwon
			won=True
			break
		if row_o_count+row.count("T")==4 and row_o_count>=3:
			print owon
			won=True
			break		
		
		mat.append(row)
	if not won:
		diag=[]
		opp_diag=[]
		for k in range(4):
			col=[mat[0][k],mat[1][k],mat[2][k],mat[3][k]]
			diag.append(mat[k][k])
			opp_diag.append(mat[k][3-k])
			col_x_count=col.count('X')
			col_o_count=col.count('O')	
			if col_x_count+col.count("T")==4 and col_x_count>=3:
				print xwon
				won=True
				break
			if col_o_count+col.count("T")==4 and col_o_count>=3:
				print  owon
				won=True
				break
		if not won:
			diag_x_count=diag.count('X')
			diag_o_count=diag.count('O')
			if diag_x_count+diag.count("T")==4 and diag_x_count>=3:
				print xwon
				won=True
				continue	
			if diag_o_count+diag.count("T")==4 and diag_o_count>=3:
				print owon
				won=True
				continue
		if not won:
			diag_x_count=opp_diag.count('X')
			diag_o_count=opp_diag.count('O')
			if diag_x_count+opp_diag.count("T")==4 and diag_x_count>=3:
				print xwon
				won=True
				continue	
			if diag_o_count+opp_diag.count("T")==4 and diag_o_count>=3:
				print owon
				won=True
				continue
		
		if not won:
			incomplete=False
			for  r in range(4):
				if mat[r].count('.')>0:
					print "Game has not completed"
					incomplete=True
					break		
			if not incomplete:
				print "Draw"