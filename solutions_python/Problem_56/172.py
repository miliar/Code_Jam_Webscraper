from sys import argv 

vertical = 0
horizontal = 1
leftd = 2
rightd = 3

def rotate(board):
	new_board = []
	for i in range(len(board)):
		row = []
		for j in range(len(board[0])):	
			row.append(board[(-1-j)][i])

		new_board.append(row)
	return new_board


def gravity(board):
	for i in range(len(board)):
		j = 0
		crop_i = 0
		crop_e = 0 
		start_crop = False
		while(j < len(board[i])):
			if(start_crop and board[i][j] == '.'):
				tmpj = j
				while(tmpj < len(board[0]) and board[i][tmpj] == '.'):
					tmpj += 1
				board[i][j:tmpj] = []
				a = ['.']*(tmpj-j)
				a.extend(board[i])
				board[i] = a
				start_crop = False
			if(board[i][j] != '.'):
				start_crop = True
			j += 1

def check(board, k):
	total = 0
	checked = [] 
	for i in range(len(board)):
		for j in range(len(board[0])):
			if(board[i][j] != '.' and not board[i][j] in checked):
				for d in range(4):
					sol = try_sol(board, i, j, k, d)
					if(sol != 0):
						total += 1
						checked.append(board[i][j])
						break
	return checked 




def try_sol(board, i, j, k, dir):
	o_i = i
	o_j = j
	my_char = board[i][j]
	corr = 1
	if(dir == vertical):
		i_dir = 1
		j_dir = 0

	if(dir == horizontal):
		i_dir = 0
		j_dir = 1
	if(dir == rightd):
		i_dir = 1
		j_dir = -1

	if(dir == leftd):
		i_dir = 1
		j_dir = 1
	j_l = len(board[0])
	i_l = len(board)

	i += i_dir
	j += j_dir
	while(j >= 0 and j< j_l and i >= 0 and i < i_l and board[i][j] == my_char and corr < k):
		j += j_dir
		i += i_dir 
		corr += 1

	i = o_i 
	j = o_j

	i -= i_dir
	j -= j_dir

	while(j >= 0 and j< j_l and i >= 0 and i < i_l and board[i][j] == my_char and corr < k):
		j -= j_dir
		i -= i_dir 
		corr += 1


	if(corr >= k):
		return 1	

	return 0


if __name__ == '__main__':

	file = open(argv[1])

	tests = int(file.readline())
	
	for m in range(tests):
		split = file.readline().split()
		n, k = int(split[0]), int(split[1])
		board = []
		for r in range(n):
			board.append(list(file.readline().strip('\n')))

		gravity(board)
		result = check(board, k)
		r_s = 'Neither'
		if(len(result) == 2):
			r_s = 'Both'
		if(len(result) == 1):
			if(result[0] == 'R'):
				r_s = 'Red'
			else:
				r_s = 'Blue'

	
		print('Case #%i: %s'%(m+1, r_s))




