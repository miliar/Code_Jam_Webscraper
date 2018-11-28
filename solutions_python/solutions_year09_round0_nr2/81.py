alf = 'abcdefghijklmnopqrstuvwxyz'
for case in range(input()):
	H, W = map(int, raw_input().split(' '))
	Map = []
	for i in range(H):
		line = map(int, raw_input().split(' '))
		Map.append(line)
	Dir = [['' for i in range(W)] for j in range(H)]
	Res = [['' for i in range(W)] for j in range(H)]
	for i in range(H):
		for j in range(W):
			min_alt = Map[i][j]
			if i > 0 and Map[i - 1][j] < min_alt:
				min_alt, Dir[i][j] = (Map[i - 1][j], 'n')
			if j > 0 and Map[i][j - 1] < min_alt:
				min_alt, Dir[i][j] = (Map[i][j - 1], 'w')
			if j < W - 1 and Map[i][j + 1] < min_alt:
				min_alt, Dir[i][j] = (Map[i][j + 1], 'e')                       
			if i < H - 1 and Map[i + 1][j] < min_alt:
				min_alt, Dir[i][j] = (Map[i + 1][j], 's')
	cur = 0
	for i in range(H):
		for j in range(W):
			if Res[i][j] != '':
				continue
			Res[i][j] = alf[cur]
			nh = [(i, j)]
			while len(nh):
				y, x = nh.pop()
				if x > 0 and Res[y][x - 1] == '' and (Dir[y][x] == 'w' or Dir[y][x - 1] == 'e'):
					Res[y][x - 1] = alf[cur]
					nh.append((y, x - 1))
				if x < W - 1 and Res[y][x + 1] == '' and (Dir[y][x] == 'e' or Dir[y][x + 1] == 'w'):
					Res[y][x + 1] = alf[cur]
					nh.append((y, x + 1))
				if y > 0 and Res[y - 1][x] == '' and (Dir[y][x] == 'n' or Dir[y - 1][x] == 's'):
					Res[y - 1][x] = alf[cur]
					nh.append((y - 1, x))
				if y < H - 1 and Res[y + 1][x] == '' and (Dir[y][x] == 's' or Dir[y + 1][x] == 'n'):
					Res[y + 1][x] = alf[cur]
					nh.append((y + 1, x))
			cur += 1				
			
	print 'Case #%s:' % (case + 1)
	for i in range(H):
		print ' '.join(Res[i])
