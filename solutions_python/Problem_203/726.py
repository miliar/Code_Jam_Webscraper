def decorate(cake, rows, cols):
	letters = list()
	frontier = 0
	for row in cake:
		for letter in row:
			if letter != '?':
				letters.append(letter)
			else:
				frontier += 1
	
	while(frontier > 0):
		'''for row in cake:
			print ''.join(row)
		print'''
		
		letter = letters.pop(0)
		#print "letter = %c" % letter

		found = False
		for r in range(rows):
			for c in range(cols):
				if cake[r][c] == letter:
					found = True
					break
			if found:
				break
		#print "r = %d, c = %d" % (r, c)

		top = r - 1
		while(top > -1):
			if cake[top][c] == '?':
				cake[top][c] = letter
				frontier -= 1
			else:
				break
			top -= 1
		#print "top = %d" % top

		left = c - 1
		while(left > -1):
			if all(cake[i][left] == '?' for i in range(r, top, -1)):
				for i in range(r, top, -1):
					cake[i][left] = letter
					frontier -= 1
			else:
				break
			left -= 1
		#print "left = %d" % left

		right = c + 1
		while(right < cols):
			if all(cake[i][right] == '?' for i in range(top+1, r+1, 1)):
				for i in range(top+1, r+1, 1):
					cake[i][right] = letter
					frontier -= 1
			else:
				break
			right += 1
		#print "right = %d" % right

		bottom = r + 1
		while (bottom < rows):
			if all(cake[bottom][j] == '?' for j in range(left+1, right, 1)):
				for j in range(left+1, right, 1):
					cake[bottom][j] = letter
					frontier -= 1
			else:
				break
			bottom += 1
		#print "bottom = %d" % bottom

	for row in cake:
		print ''.join(row)
	return

if __name__ == '__main__':
    for T in range(int(raw_input().strip())):
        row, col = (int(n) for n in raw_input().strip().split())
        cake = list()
        for i in range(row):
        	cake.append(list(raw_input()))
        print "Case #%d:" % (T+1)
        decorate(cake, row, col)