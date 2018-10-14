input = open('large.in', 'r')
output = open('large.out', 'w');

cases = int(input.readline())

i=0
while i < cases:
	
	table = []
	
	j = 0
	while j < 4:
		
		line = input.readline()
		line = list(line)
		
		table2 = []
		
		k = 0
		while k < 4:
			table2.append(line[k])
			k = k + 1
		
		table.append(table2)
		
		j = j + 1
	
	
	oNoWin = 1
	xNoWin = 1
	es = 0
	
	j = 0
	while (j < 4) and oNoWin and xNoWin:
		print "pass 1"
		
		cX = 0
		cO = 0
		
		k = 0
		while k < 4:
			op = table[j][k]
			
			if op == "X":
				cX = cX +1
			else:
				if op == "O":
					cO = cO + 1
				else:
					if op == "T":
						cX = cX + 1
						cO = cO + 1
					else:
						es = es + 1
			
			k = k + 1
		
		if (cO == 4):
			oNoWin = 0
		else:
			if (cX == 4):
				xNoWin = 0
		j = j + 1
		
	j = 0
	while (j < 4) and oNoWin and xNoWin:
		print "pass 2"
		cX = 0
		cO = 0
		
		k = 0
		while k < 4:
			op = table[k][j]
			
			if op == "X":
				cX = cX +1
			else:
				if op == "O":
					cO = cO + 1
				else:
					if op == "T":
						cX = cX + 1
						cO = cO + 1
					else:
						es = es + 1
			
			k = k + 1
		
		if (cO == 4):
			oNoWin = 0
		else:
			if (cX == 4):
				xNoWin = 0
		j = j + 1
		
	j = 0
	cX = 0
	cO = 0	
	while (j < 4) and oNoWin and xNoWin:
		print "pass 3"
		
		op = table[j][j]
		
		if op == "X":
			cX = cX + 1
		else:
			if op == "O":
				cO = cO + 1
			else:
				if op == "T":
					cX = cX + 1
					cO = cO + 1
				else:
					es = es + 1
		print "cO: "+str(cO)
		
		if (cO == 4):
			oNoWin = 0
		else:
			if (cX == 4):
				xNoWin = 0
		j = j + 1
		
	j = 0
	cX = 0
	cO = 0	
	while (j < 4) and oNoWin and xNoWin:
		print "pass 4"
		
		op = table[j][3-j]
		
		if op == "X":
			cX = cX + 1
		else:
			if op == "O":
				cO = cO + 1
			else:
				if op == "T":
					cX = cX + 1
					cO = cO + 1
				else:
					es = es + 1
		
		if (cO == 4):
			oNoWin = 0
		else:
			if (cX == 4):
				xNoWin = 0
		j = j + 1
	
	if not oNoWin:
		result = "O won"
	else:
		if not xNoWin:
			result = "X won"
		else:
			if not es:
				result = "Draw"
			else:
				result = "Game has not completed"
				
	output.write("Case #"+str(i+1)+": "+result+"\n")
	
	space = input.readline()
	print " ";
	i = i + 1