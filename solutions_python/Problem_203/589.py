def fillc(mat, r, c):
	cnt = 0
	ur, dr = r-1, r+1
	while ur >=0 and mat[ur][c] == '?':
		mat[ur][c] = mat[r][c]
		ur -= 1
		cnt += 1
					
	while dr < len(mat) and mat[dr][c] == '?':
		mat[dr][c] = mat[r][c]
		dr += 1
		cnt += 1
	
	return cnt

def fillr(mat, r, c):
	cntl, cntr = 0, 0
	lc, rc = c-1, c+1
	while lc >=0 and mat[r][lc] == '?':
		mat[r][lc] = mat[r][c]
		lc -= 1
		cntl += 1
					
	while rc < len(mat[0]) and mat[r][rc] == '?':
		mat[r][rc] = mat[r][c]
		rc += 1
		cntr += 1
	
	return cntl, cntr
	
			
	
case = int(raw_input())
for cn in range(1, case+1):
	line = [int(s) for s in raw_input().split(" ")]
	R, C = line[0], line[1]
	mat = []
	for i in range(R):
		r =  raw_input()
		mat.append(list(r))
	
	
	while True:
		numq = 0
		r, c = 0, 0
		while r < R:
			c = 0
			while c < C:
				if mat[r][c] == '?':
					numq += 1
					c += 1
					continue
				
				lf, rf = fillr(mat, r, c)
				#if lf + rf == 0:
					#fillc(mat, r, c)
				c += rf + 1
			r += 1
		
		if numq == 0:
			break
			
		numq = 0
		r, c = 0, 0
		while r < R:
			c = 0
			while c < C:
				if mat[r][c] == '?':
					numq += 1
					c += 1
					continue
				
				fillc(mat, r, c)
				#if lf + rf == 0:
					#fillc(mat, r, c)
				c += 1
			r += 1
		if numq == 0:
			break
		
		
		
	print "Case #"+str(cn)+":"
	for i in range(R):
		print "".join(mat[i])
		