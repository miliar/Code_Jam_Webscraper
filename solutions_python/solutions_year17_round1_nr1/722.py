for t in range(int(input())):
	r,c = [int(i) for i in input().split()]
	s = []
	for i in range(r):
		s.append(list(input()))
	s1 = []
	for i in range(r):
		a = []
		for j in range(c):
			a.append(s[i][j])
		s1.append(a)
	def fill(left,right,i,ini):
		for k in range(i,r):
			f = 0
			for j in range(left,right + 1):
				if s[k][j] != '?':
					if s[k][j] != ini:
						f = 1
						break
			if f == 1:
				break
			for j in range(left,right + 1):
				s1[k][j] = ini
	def fill_up(left,right,i,ini):
		for k in range(0,i + 1):
			for j in range(left,right + 1):
				s1[k][j] = ini
	flag = 0
	for i in range(r):
		for j in range(c):
			if s[i][j] != '?':
				left = right = 0
				top = bottom = 0
				x = j
				while True:
					x -= 1;
					if x < 0:
						break
					if s1[i][x] != '?' and s1[i][x] != s[i][j]:
						break
				left = x + 1
				x = j
				while True:
					x += 1;
					if x > c - 1:
						break
					if s1[i][x] != '?' and s1[i][x] != s[i][j]:
						break
				right = x - 1
				#print(left,right)
				fill(left,right,i,s[i][j])
				if i > 0 and s1[i - 1][j] == '?':
					fill_up(left,right,i,s[i][j])
					flag = 1
	print("Case #{}:".format(t+1))
	for i in range(r):
		[print(j,end = '') for j in s1[i]]
		print()