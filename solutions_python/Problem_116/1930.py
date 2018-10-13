input = 'C:\\Users\\William\\Desktop\\A-large.in'

f = open(input, "r")
cases = f.readline()

count = 1

for x in range(int(cases)):
	X_won = 0
	O_won = 0
	
	line1 = f.readline()
	line2 = f.readline()
	line3 = f.readline()
	line4 = f.readline()
	blank = f.readline()
	
	col = {}
	for i in range(4):
		col[i] = line1[i] + line2[i] + line3[i] + line4[i]
	
	diag1 = line1[0] + line2[1] + line3[2] + line4[3]
	diag2 = line1[3] + line2[2] + line3[1] + line4[0]
	
	if line1.count('X')==4 or line2.count('X')==4 or line3.count('X')==4 or line4.count('X')==4 or diag1.count('X')==4 or diag2.count('X')==4:
		X_won = 1
		print "Case #"+str(count)+": X won"
		count += 1
		continue
		
	if line1.count('O')==4 or line2.count('O')==4 or line3.count('O')==4 or line4.count('O')==4 or diag1.count('O')==4 or diag2.count('O')==4:
		O_won = 1
		print "Case #"+str(count)+": O won"
		count += 1
		continue
		
	if (line1.count('X')==3 and line1.count('T')==1) or (line2.count('X')==3 and line2.count('T')==1) or (line3.count('X')==3 and line3.count('T')==1) or (line4.count('X')==3 and line4.count('T')==1) or (diag1.count('X')==3 and diag1.count('T')==1) or (diag2.count('X')==3 and diag2.count('T')==1):
		X_won = 1
		print "Case #"+str(count)+": X won"
		count += 1
		continue
		
	if (line1.count('O')==3 and line1.count('T')==1) or (line2.count('O')==3 and line2.count('T')==1) or (line3.count('O')==3 and line3.count('T')==1) or (line4.count('O')==3 and line4.count('T')==1) or (diag1.count('O')==3 and diag1.count('T')==1) or (diag2.count('O')==3 and diag2.count('T')==1):
		O_won = 1
		print "Case #"+str(count)+": O won"
		count += 1
		continue
		
	for c in col:
		if col[c].count('X')==4:
			X_won = 1
			print "Case #"+str(count)+": X won"
			count +=1
			break
		if col[c].count('O')==4:
			O_won = 1
			print "Case #"+str(count)+": O won"
			count += 1
			break
		if col[c].count('X')==3 and col[c].count('T')==1:
			X_won = 1
			print "Case #"+str(count)+": X won"
			count +=1
			break
		if col[c].count('O')==3 and col[c].count('T')==1:
			O_won = 1
			print "Case #"+str(count)+": O won"
			count += 1
			break
	
	if X_won==0 and O_won==0 and ('.' in line1 or '.' in line2 or '.' in line3 or '.' in line4):
		print "Case #"+str(count)+": Game has not completed"
		count += 1
	elif X_won==0 and O_won==0 and ('.' not in line1 or '.' not in line2 or '.' not in line3 or '.' not in line4):
		print "Case #"+str(count)+": Draw"
		count += 1
		