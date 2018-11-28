import sys

casesN = 0;
mycases = [];
outputFile = open("output.txt", "w");

def getCases(filename):
	try:
		casesFile = open(filename, "r")
	except:
		print "File", filename, "could not be opened!\n"
		exit(1)
		
	global casesN, mycases;
	
	casesN=int(casesFile.readline())
	
	for i in range(casesN):
		curCase = []
		for j in range(4):
			curLine = casesFile.readline()
			curLine = curLine[:-1]
			curCase.append(curLine);
		casesFile.readline();
		mycases.append(curCase)
		
def winnerOf(Wtype):
	if(Wtype=="X"):
		return "X won"
	elif(Wtype=="O"):
		return "O won"
	elif(Wtype=="draw"):
		return "Draw"
	elif(Wtype=="unfinished"):
		return "Game has not completed"

def hasDot(array):
	for i in range(4):
		for j in range(4):
			if(array[i][j]=="."):
				return True;
	return False;

def determineWinner():
	winner=""
	for k in range(casesN):
		curCase = mycases[k];
		for i in range(4):
			#checking all lines
			if(curCase[i][0]==curCase[i][1]==curCase[i][2]==curCase[i][3]!="."):
				winner=winnerOf(curCase[i][0]);
				break;
			elif(curCase[i][0]=="T"):
				if(curCase[i][1]==curCase[i][2]==curCase[i][3]!="."):
					winner=winnerOf(curCase[i][1]);
					break;
			elif(curCase[i][1]=="T"):
				if(curCase[i][0]==curCase[i][2]==curCase[i][3]!="."):
					winner=winnerOf(curCase[i][0]);
					break;
			elif(curCase[i][2]=="T"):
				if(curCase[i][0]==curCase[i][1]==curCase[i][3]!="."):
					winner=winnerOf(curCase[i][0]);
					break;
			elif(curCase[i][3]=="T"):
				if(curCase[i][0]==curCase[i][1]==curCase[i][2]!="."):
					winner=winnerOf(curCase[i][0]);
					break;
			
			#checking all columns
			
			if(curCase[0][i]==curCase[1][i]==curCase[2][i]==curCase[3][i]!="."):
				winner=winnerOf(curCase[0][i]);
				break;
			elif(curCase[0][i]=="T"):
				if(curCase[1][i]==curCase[2][i]==curCase[3][i]!="."):
					winner=winnerOf(curCase[1][i]);
					break;
			elif(curCase[1][i]=="T"):
				if(curCase[0][i]==curCase[2][i]==curCase[3][i]!="."):
					winner=winnerOf(curCase[0][i]);
					break;
			elif(curCase[2][i]=="T"):
				if(curCase[0][i]==curCase[1][i]==curCase[3][i]!="."):
					winner=winnerOf(curCase[0][i]);
					break;
			elif(curCase[3][i]=="T"):
				if(curCase[0][i]==curCase[1][i]==curCase[2][i]!="."):
					winner=winnerOf(curCase[0][i]);
					break;
			
			#checking leftovers
			
			if(curCase[0][0]==curCase[1][1]==curCase[2][2]==curCase[3][3]!="."):
				winner=winnerOf(curCase[0][0])
				break;
			elif(curCase[0][0]=="T"):
				if(curCase[1][1]==curCase[2][2]==curCase[3][3]!="."):
					winner=winnerOf(curCase[1][1])
					break;
			elif(curCase[1][1]=="T"):
				if(curCase[0][0]==curCase[2][2]==curCase[3][3]!="."):
					winner=winnerOf(curCase[0][0])
					break;
			elif(curCase[2][2]=="T"):
				if(curCase[0][0]==curCase[1][1]==curCase[3][3]!="."):
					winner=winnerOf(curCase[0][0])
					break;
			elif(curCase[3][3]=="T"):
				if(curCase[0][0]==curCase[1][1]==curCase[2][2]!="."):
					winner=winnerOf(curCase[0][0])
					break;
					
			if(curCase[0][3]==curCase[1][2]==curCase[2][1]==curCase[3][0]!="."):
				winner=winnerOf(curCase[0][3])
				break;
			elif(curCase[0][3]=="T"):
				if(curCase[1][2]==curCase[2][1]==curCase[3][0]!="."):
					winner=winnerOf(curCase[1][2])
					break;
			elif(curCase[1][2]=="T"):
				if(curCase[0][3]==curCase[2][1]==curCase[3][0]!="."):
					winner=winnerOf(curCase[0][3])
					break;
			elif(curCase[2][1]=="T"):
				if(curCase[0][3]==curCase[1][2]==curCase[3][0]!="."):
					winner=winnerOf(curCase[0][3])
					break;
			elif(curCase[3][0]=="T"):
				if(curCase[0][3]==curCase[1][2]==curCase[2][1]!="."):
					winner=winnerOf(curCase[0][3])
					break;
			
			#winner has yet to be found, if there is dot, then game's not over, if there is not dot, it is draw.
			if(hasDot(curCase)):
				winner=winnerOf("unfinished");
			else:
				winner=winnerOf("draw");
			
		outputFile.write("Case #"+str(k+1)+": "+winner+"\n");
	outputFile.close();

def main():
	if(len(sys.argv)!=2):
		print "No input file specified"
		exit(1)
	
	getCases(sys.argv[1]);
	
	determineWinner();
	
main();
