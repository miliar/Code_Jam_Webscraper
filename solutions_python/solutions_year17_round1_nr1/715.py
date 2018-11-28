z = []
for jsfsdkfj in range(int(input())):
	r, c = map(int, input().split())
	l = []
	d = []
	flag = 0
	for i in range(r):
		l.append(list(input()))
	for i in l:
		d.append(i.copy())
	for k,j in enumerate(l):
		for cn,i in enumerate(j):
			if (k==0 and i=='?'):
				for k2 in range(k+1,r):
					if (l[k2][cn]!='?'):
						l[k][cn] = l[k2][cn]
						break
			elif (i=='?'):
				for k2 in range(k-1,-1, -1):
					if (l[k2][cn]!='?'):
						l[k][cn] = l[k2][cn]
						break
	for i in l:
		if '?' in i:
			flag = 1
	if flag==1:
		l = list(map(list, zip(*d)))
		for k,j in enumerate(l):
			for cn,i in enumerate(j):
				if (k==0 and i=='?'):
					for k2 in range(k+1,c):
						if (l[k2][cn]!='?'):
							l[k][cn] = l[k2][cn]
							break
				elif (i=='?'):
					for k2 in range(k-1,-1, -1):
						if (l[k2][cn]!='?'):
							l[k][cn] = l[k2][cn]
							break
		l = list(map(list, zip(*l)))
	for i in l:
		if '?' in i:
			flag = 2
	if flag == 2:
		for k,j in enumerate(l):
			for cn,i in enumerate(j):
				if (k==0 and i=='?'):
					for k2 in range(k+1,r):
						if (l[k2][cn]!='?'):
							l[k][cn] = l[k2][cn]
							break
				elif (i=='?'):
					for k2 in range(k-1,-1, -1):
						if (l[k2][cn]!='?'):
							l[k][cn] = l[k2][cn]
							break
	z.append(l)
for c,i in enumerate(z):
	print("Case #" + str(c+1) + ":")
	for a in i:
		print(''.join(a))
