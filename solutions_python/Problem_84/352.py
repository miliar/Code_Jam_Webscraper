#coding:utf-8
import sys
def showlist(lst):
	for line in lst:
		print line

#fin = open("ainput.txt")
fin = open("A-large.in")
fout = open("aoutput.txt","w")
cases = int(fin.readline())
for case in xrange(1,cases+1):
	ans = ("")
	R,C = map(int, fin.readline().split()) #多数の整数を読み込む
	board = [list(fin.readline().rstrip()) for i in xrange(R)] #M行にわたるテキストを読み込む
	#showlist(board)
	for i in xrange(R-1):
		for j in xrange(C-1):
			if board[i][j] == "#":
				if board[i+1][j] == board[i][j+1] == board[i+1][j+1] == "#":
					board[i][j] = "/"
					board[i+1][j] = "*"
					board[i][j+1] = "*"
					board[i+1][j+1] = "/"
				else:
					ans = "\nImpossible"
			if not ans == "":
				break
		if not ans == "":
			break
#	print ans
#	showlist(board)
	if ans == "" :
		ans = "\n"
		for line in board:
			ans += "".join(line).replace("*",u"\\")+"\n"
			if "#" in ans:
				ans = "\nImpossible\n"
				break
	ans = ans.rstrip("\n")
	result = "Case #"+str(case)+": "+ans
	print result
	fout.write(result+"\n")

fin.close()
fin.close()



