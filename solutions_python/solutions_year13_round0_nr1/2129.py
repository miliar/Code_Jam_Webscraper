#!/usr/bin/python
val={'X':2,'O':0,'.':0.33,'T':1}
def Sum(row,board):
	s=0
	for i in row:
		s+=val[board[i]]
	return s
def Check(row,board):
	for i in row:
		if val[board[i]] == 0.33:
			return True
def winner(n,board):
	flag={}
        """Determine if one player has won the game. Returns Player_X, Player_O or None"""
        winning_rows = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]] 
        for row in winning_rows:
            if Sum(row,board) == 1 or Sum(row,board) == 0:
		flag['A']='Case #'+str(n)+': O won'
	    elif Sum(row,board) == 8 or Sum(row,board) == 7	:
		flag['B']='Case #'+str(n)+': X won'
	    elif Check(row,board):
	        flag['C']='Case #'+str(n)+': Game has not completed'
	if len(flag.keys()) == 0:
		flag['D']='Case #'+str(n)+': Draw'
	return flag	
def main():
	 n=int(raw_input())
	 for i in range(n):
		 board = [[j for j in raw_input().strip()] for l in range(4)]
		 temp=raw_input()
		 for j in board[1:]:
			 board[0].extend(j)
		 board= board[0]
		 flag=winner(i+1,board)
		 for key in sorted(flag.keys()):
			 print flag[key]
			 break

if __name__ == "__main__":
	main()
