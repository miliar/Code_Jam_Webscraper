import sys
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")


for t in range(int(input())) : 
	print('Case #',t+1,':',sep = '')
	r,c = map(int,input().split())
	g = [list(input())  for i in range(r)]
	d = {}
	for i in range(r) : 
		for j in range(c) : 
			if g[i][j] != '?' : 
				d[g[i][j]] = [i,j]

	for a in d : 
		x = d[a][1] ; y = d[a][0]
		j = x+1
		while j < c and g[y][j] == '?' : 
			g[y][j ] = a
			j += 1
		j = x
		while j > 0 and g[y][j-1] == '?' : 
			g[y][j-1 ] = a
			j -= 1
	ls = []
	b = [False]*r
	for i in range(r) :		
		if g[i].count('?') != c : 
			ls.append(i)
			b[i] = True
	
	for i in ls : 
		y = i-1
		while y >=  0 and b[y] == False : 
			g[y] = g[i]
			y -= 1
		y = i+1
		while y < r and b[y] == False : 
			g[y] = g[i]
			y += 1
	for i in range(r) : 
		print(''.join(g[i]))		
			