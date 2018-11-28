def flip(s,i,n):
	for j in range(n):
		s[i+j]=1-s[i+j]



n_cases=input()
for t in range(int(n_cases)):
	input_string=input().split()
	board=[1 if c=='+' else 0 for c in input_string[0]]
	flip_size=int(input_string[1])

	counter=0
	for i in range(len(board)-flip_size+1):
		if board[i]==0:
			flip(board,i,flip_size)
			counter+=1

	if sum(board)==len(board):
		print('Case #%d: %d' % (t+1, counter))
	else:
		print('Case #%d: IMPOSSIBLE' % (t+1))
