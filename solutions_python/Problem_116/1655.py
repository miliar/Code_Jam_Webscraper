'''

    "X won" (the game is over, and X won)
    "O won" (the game is over, and O won)
    "Draw" (the game is over, and it ended in a draw)
    "Game has not completed" (the game is not over yet)
    
    Case #1: X won
	Case #2: Draw
	Case #3: Game has not completed
	Case #4: O won
	Case #5: O won
	Case #6: O won

'''


import os
import sys
import pdb
from os.path import basename

ttt_matrix = []

def getResult(fo, mlist, index):	
	global ttt_matrix
	dot_flag=0
	s = (5*index)-4	
	e = s+3
	if e>=len(mlist) or s>=len(mlist):
		print "Out of bound error"				
		return
	for i in range(s,e+1):		
		ttt_matrix.append([mlist[i][0],mlist[i][1], mlist[i][2], mlist[i][3]])	
	
	# check row 
	#pdb.set_trace()
	for i in range(4):
		if (ttt_matrix[i].count('X')==3 and ttt_matrix[i].count('T')==1) or ttt_matrix[i].count('X')==4:
			fo.write("Case #"+str(index)+": X won\n")
			return
		elif (ttt_matrix[i].count('O')==3 and ttt_matrix[i].count('T')==1) or ttt_matrix[i].count('O')==4:
			fo.write("Case #"+str(index)+": O won\n")
			return 
		elif ttt_matrix[i].count('.')>=1:
			dot_flag=1			
	
	#check column
	for j in range(4):
		temp = []
		for i in range(4):
			temp.append(ttt_matrix[i][j])
		if (temp.count('X')==3 and temp.count('T')==1) or temp.count('X')==4:
			fo.write("Case #"+str(index)+": X won\n")
			return
		elif (temp.count('O')==3 and temp.count('T')==1) or temp.count('O')==4:
			fo.write("Case #"+str(index)+": O won\n")
			return 
		elif temp.count('.')>=1:
			dot_flag=1
			
	#check diagonal & cross diagonal
	dg=[]
	cdg=[]
	for i in range(4):		
		dg.append(ttt_matrix[i][i])
		cdg.append(ttt_matrix[i][3-i])
	if (dg.count('X')==3 and dg.count('T')==1) or dg.count('X')==4:
		fo.write("Case #"+str(index)+": X won\n")
		return
	elif (dg.count('O')==3 and dg.count('T')==1) or dg.count('O')==4:
		fo.write("Case #"+str(index)+": O won\n")
		return 
	elif dg.count('.')>=1:
		dot_flag=1
	
	#pdb.set_trace()
	if (cdg.count('X')==3 and cdg.count('T')==1) or cdg.count('X')==4:
		fo.write("Case #"+str(index)+": X won\n")
		return
	elif (cdg.count('O')==3 and cdg.count('T')==1) or cdg.count('O')==4:
		fo.write("Case #"+str(index)+": O won\n")
		return 
	elif cdg.count('.')>=1:
		dot_flag=1
		
    # if no one wining, check whether game is finished
	if dot_flag == 1:
		fo.write("Case #"+str(index)+": Game has not completed\n")
		return
	else:
		fo.write("Case #"+str(index)+": Draw\n")
		return
	
	return


if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit()
	
with open(sys.argv[1], 'r') as f:
	read_data = f.readlines()	

fo = open(os.path.splitext(basename(sys.argv[1]))[0]+".out", 'w')
# Extract test_case
test_case = int(read_data[0])


if test_case > 1000 or test_case < 1:
	sys.exit()
	
for i in range(test_case):
	ttt_matrix = []
	getResult(fo,read_data, i+1)
	

f.close()
fo.close()
	
	



