n = int(raw_input())
for k in range(n):
	board = []

	def find_winner(word):
		if (word.count('X') == 3 and word.count("T")==1) or word.count('X') == 4: return "X won"
		if (word.count('O') == 3 and word.count("T")==1) or word.count('O') == 4: return "O won"
		return "Draw"
	for i in range(4):
		board.append(list(raw_input()))
	palavras = ['']*10
	count_ponto = 0
	for i in range(4):
		palavras[i]= "".join(board[i])
		for j in range(4):
			palavras[j+4]+= board[i][j]
			if i==j:
				palavras[8]+= board[i][j]
			if 3-j == i:
				palavras[9]+= board[i][j]
		count_ponto+=palavras[i].count('.')
	msg = ''
	for p in palavras:
		tmp = find_winner(p)
		if "won" not in msg: msg = tmp
	if count_ponto > 0 and "Draw" in msg: msg = "Game has not completed"
	print "Case #"+str(k+1) +": "+msg
	if k!=n-1: raw_input()
