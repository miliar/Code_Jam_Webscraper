T = input()
for t in range(T):
	R, C = map(int, raw_input().split())
	chars = {}
	cake = []
	for r in range(R):
		line = raw_input()
		cake.append(line)
		for c in range(C):
			if line[c] != '?':
				chars[line[c]] = (c, r)
	for char in chars:
		x, y = chars[char]
		cur_x = x -1
		while cur_x >= 0 and cake[y][cur_x] == '?':
			cur_x = cur_x -1
		low_x = cur_x + 1		
		cur_x = x + 1
		while cur_x < C and cake[y][cur_x] == '?':
			cur_x = cur_x + 1
		high_x = cur_x - 1		
		width = high_x - low_x + 1

		cake[y] = cake[y][0:low_x] + char*width + cake[y][high_x+1:]

		cur_y = y - 1
		while cur_y >= 0 and cake[cur_y][low_x:high_x+1] == '?'*width:
			cake[cur_y] = cake[cur_y][0:low_x] + char*width + cake[cur_y][high_x+1:]
			cur_y = cur_y - 1		
		cur_y = y + 1
		while cur_y < R and cake[cur_y][low_x:high_x+1] == '?'*width:
			cake[cur_y] = cake[cur_y][0:low_x] + char*width + cake[cur_y][high_x+1:]
			cur_y = cur_y + 1		

	print 'Case #' + str(t+1) +':'
	for line in cake:
		print line
