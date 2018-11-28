f=open("A-large.in","r")
g=open("write_1.out","w")
content=f.read()
content=content.split()
T=int(content[0])
for t in xrange(1,T+1):
	table=[]
	for j in range(1,5):
		table.append(content[4*t+j-4])
	print table
	#vertical
	for j in range(4):
		O_count=0
		X_count=0
		for i in range(4):
			if table[i][j]=='T':
				O_count+=1
				X_count+=1
			if table[i][j]=='O':
				O_count+=1
			if table[i][j]=='X':
				X_count+=1
		if X_count==4:
			g.write("Case #"+str(t)+": X won\n")
			break
		if O_count==4:
			g.write("Case #"+str(t)+": O won\n")
			break
	if X_count==4 or O_count==4:
		continue

	#horizontal
	for j in range(4):
		O_count=0
		X_count=0
		for i in range(4):
			if table[j][i]=='T':
				O_count+=1
				X_count+=1
			if table[j][i]=='O':
				O_count+=1
			if table[j][i]=='X':
				X_count+=1
		if X_count==4:
			g.write("Case #"+str(t)+": X won\n")
			break
		if O_count==4:
			g.write("Case #"+str(t)+": O won\n")
			break
	if X_count==4 or O_count==4:
		continue

	#diag1
	O_count=0
	X_count=0
	for i in range(4):
		
		if table[i][i]=='T':
			O_count+=1
			X_count+=1
		if table[i][i]=='O':
			O_count+=1
		if table[i][i]=='X':
			X_count+=1
	if X_count==4:
		g.write("Case #"+str(t)+": X won\n")
		continue
	if O_count==4:
		g.write("Case #"+str(t)+": O won\n")
		continue

	#diag2
	O_count=0
	X_count=0
	for i in range(4):
		
		if table[i][3-i]=='T':
			O_count+=1
			X_count+=1
		if table[i][3-i]=='O':
			O_count+=1
		if table[i][3-i]=='X':
			X_count+=1
	if X_count==4:
		g.write("Case #"+str(t)+": X won\n")
		continue
	if O_count==4:
		g.write("Case #"+str(t)+": O won\n")
		continue
		

	count=0
	for i in range(4):
		for j in range(4):
			if table[i][j]=='.':
				count+=1
	if count==0:
		g.write("Case #"+str(t)+": Draw\n")
		continue

	g.write("Case #"+str(t)+": Game has not completed\n")

f.close()
g.close()