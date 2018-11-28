import operator
import math

def get_winner(line):
	#if (line[0]=="O" && line[1]=="O" && line[2]=="O" && line[3]=="O")
	#print line.find("O") !=-1
	if (line.find("O") != -1 and line.find("X")!= -1) or line.find(".")!= -1:
		return "No Winner"
	elif line.find("O")!=-1:
		return "O won"
	else:
		return "X won"
		
		
def get_game_winner(line):
	if (line[0].find(".")==-1 and line[1].find(".")==-1 and line[2].find(".")==-1 and line[3].find(".")==-1):
		complete = 1
	else:
		complete = 0
	#check rows
	columns = [line[0][0]+line[1][0]+line[2][0]+line[3][0],line[0][1]+line[1][1]+line[2][1]+line[3][1],line[0][2]+line[1][2]+line[2][2]+line[3][2],line[0][3]+line[1][3]+line[2][3]+line[3][3]]
	horizontals = [line[0][0]+line[1][1]+ line[2][2]+ line[3][3], line[0][3]+line[1][2]+line[2][1]+line[3][0]]
	line = line + columns + horizontals
	for item in line:
	
		winner = get_winner(item)
		#print winner
		#print "checking winner"
		if winner=="O won" or winner=="X won":
			break
	
	#check columns

	
	if complete == 1:
		if winner=="O won" or winner=="X won":
			return winner
		else:
			return "Draw"
	else:
		if winner=="O won" or winner=="X won":
			return winner
		else:
			return "Game has not completed"
		
	
lines = [i.strip() for i in open("input.txt").readlines()]
f = open('outputsmall.txt','w')
num_cases = int(float(lines[0]));
c = 1
i = 1

while i<len(lines):
    	#print lines[i]
	#print lines[i+1]
	#print lines[i+2]
	#print lines[i+3]
	
	board = [lines[i],lines[i+1],lines[i+2],lines[i+3]]
	#print board
	
	#check rows
	#print get_game_winner(board)
	
	
	
	f.write("Case #" +str(c) +": " + get_game_winner(board) + '\n') 
	#print "Case #" +str(c) +":", get_game_winner(board)
	c = c + 1
	i= i + 5