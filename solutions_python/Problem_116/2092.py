import sys

file = open(sys.argv[1])
T = int(file.readline())
for X in range(1,T+1):
	a = []
	incomplete = 0
	winner = 'M'
	for i in range(4):
		a.append(file.readline())
	file.readline()
	for i in range(4):
		for j in range(4):
			if a[i][j] == '.':
				incomplete = 1
			else:
				if i == 0:
					if a[i][j] == 'T' or a[i+1][j] == 'T' or a[i+1][j] == a[i][j]:
						if a[i+1][j]!='.':
							if a[i+2][j] == 'T' or a[i+2][j] == a[i+1][j] or a[i+2][j] == a[i][j]:
								if a[i+3][j] == 'T' or a[i+3][j] == a[i+1][j] or a[i+3][j] == a[i][j]:
									if a[i][j] == 'T':
										winner = a[i+1][j]
									else:
										winner = a[i][j]
									break
				if j == 0:
					if a[i][j] == 'T' or a[i][j+1] == 'T' or a[i][j+1] == a[i][j]:
						if a[i][j+1] != '.':
							if a[i][j+2] == 'T' or a[i][j+2] == a[i][j+1] or a[i][j+2] == a[i][j]:
								if a[i][j+3] == 'T' or a[i][j+3] == a[i][j+1] or a[i][j+3] == a[i][j]:
									if a[i][j] == 'T':
										winner = a[i][j+1]
									else:
										winner = a[i][j]
									break
				if i == 0 and j == 0:
					if a[i][j] == 'T' or a[i+1][j+1] == 'T' or a[i+1][j+1] == a[i][j]:
						if a[i+1][j+1] != '.':
							if a[i+2][j+2] == 'T' or a[i+2][j+2] == a[i+1][j+1] or a[i+2][j+2] == a[i][j]:
								if a[i+3][j+3] == 'T' or a[i+3][j+3] == a[i+1][j+1] or a[i+3][j+3] == a[i][j]:
									if a[i][j] == 'T':
										winner = a[i+1][j+1]
									else:
										winner = a[i][j]
									break	
				if i == 0 and j == 3:
					if a[i][j] == 'T' or a[i+1][j-1] == 'T' or a[i+1][j-1] == a[i][j]:
						if a[i+1][j-1] != '.':
							if a[i+2][j-2] == 'T' or a[i+2][j-2] == a[i+1][j-1] or a[i+2][j-2] == a[i][j]:
								if a[i+3][j-3] == 'T' or a[i+3][j-3] == a[i+1][j-1] or a[i+3][j-3] == a[i][j]:
									if a[i][j] == 'T':
										winner = a[i+1][j-1]
									else:
										winner = a[i][j]
									break
		else:
			continue;
		break;
	if winner != 'M':
		print("Case #"+str(X)+": "+str(winner)+" won")
	else:
		if incomplete == 0:
			print("Case #"+str(X)+": Draw")
		else:
			print("Case #"+str(X)+": Game has not completed")
