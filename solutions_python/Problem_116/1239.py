fileIn = open("A-large.in","r")
fileOut = open("A-large.out","w")
lines = fileIn.readlines()
fileIn.close()
cases = int(lines[0])

table=[["","","",""],["","","",""],["","","",""],["","","",""]]

k=1
countX=0
countO=0
for t in range(0,cases):
	empty=0
	finish=False
	for i in range(0,4):
		table[i]=list(lines[k][:-1])
		k+=1
	#row
	for i in range(0,4):
		countX=0
		countO=0
		if "X" in table[i] or "O" in table[i] :
			for j in range(0,4):
				if table[i][j]=="X":
					countX+=1
				elif table[i][j]=="O":
					countO+=1
				elif table[i][j]=="T":
					countX+=1
					countO+=1
			if countX==4:
				fileOut.write("Case #"+str(t+1)+": X won\n")
				finish=True
				break
			elif countO==4:
				fileOut.write("Case #"+str(t+1)+": O won\n")
				finish=True
				break 
	if not finish:				
		#column					
		for i in range(0,4):
			countX=0
			countO=0	
			Col = [table[0][i],table[1][i],table[2][i],table[3][i]]
			if "X" in Col or "O" in Col:
				for j in range(0,4):
					if Col[j]=="X":
						countX+=1
					elif Col[j]=="O":
						countO+=1
					elif Col[j]=="T":
						countX+=1
						countO+=1
				if countX==4:
					fileOut.write("Case #"+str(t+1)+": X won\n")
					finish=True
					break
				elif countO==4:
					fileOut.write("Case #"+str(t+1)+": O won\n")
					finish=True
					break				
		
		if not finish:
			#diagonal
			countX=0
			countO=0			
			diag1 = [table[0][0],table[1][1],table[2][2],table[3][3]]
			diag2 = [table[3][0],table[2][1],table[1][2],table[0][3]]
			if "X" in diag1 or "O" in diag1:
				for j in range(0,4):
					if diag1[j]=="X":
						countX+=1
					elif diag1[j]=="O":
						countO+=1
					elif diag1[j]=="T":
						countX+=1
						countO+=1
				if countX==4:
					fileOut.write("Case #"+str(t+1)+": X won\n")
					finish=True
					
				elif countO==4:
					fileOut.write("Case #"+str(t+1)+": O won\n")
					finish=True
					

			if not finish:	
				countX=0
				countO=0
				if "X" in diag2 or "O" in diag2:
					for j in range(0,4):
						if diag2[j]=="X":
							countX+=1
						elif diag2[j]=="O":
							countO+=1
						elif diag2[j]=="T":
							countX+=1
							countO+=1
					if countX==4:
						fileOut.write("Case #"+str(t+1)+": X won\n")
						finish=True

					elif countO==4:
						fileOut.write("Case #"+str(t+1)+": O won\n")
						finish=True


				if not finish:
					for i in range(0,4):
						if "." in table[i]:
							empty=1

					if empty==1:
						fileOut.write("Case #"+str(t+1)+": Game has not completed\n")
					else:
						fileOut.write("Case #"+str(t+1)+": Draw\n")
	k+=1
fileOut.close()
