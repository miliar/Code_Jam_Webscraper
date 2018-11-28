T = int(input())
for iT in list(range(0, T)):
	lim = input().split()
	N = int(lim[0])
	M = int(lim[1])
	a = []
	for i in list(range(0, N)):
		a.append(list(input()))
	cnt = 0
	for i in list(range(0, N)):
		for j in list(range(0, M)):
			if (a[i][j] == '?'):
				cnt = cnt + 1
	while (cnt > 0):
		for i in list(range(0, N)):
			for j in list(range(0, M)):
				if (a[i][j] != '?'):
					orig = a[i][j]

					if (j + 1 < M):
						if (a[i][j+1] == '?'):
							l = i
							r = i
							while ((l >= 0) and (a[l][j] == orig)):
								l = l - 1
							while ((r < N) and (a[r][j] == orig)):
								r = r + 1
							flag = True
							for z in list(range(l+1, r)):
								if (a[z][j+1] != '?'):
									flag = False
							if flag:
								for z in list(range(l+1, r)):
									a[z][j+1] = orig
									cnt = cnt - 1

					if (j - 1 >= 0):
						if (a[i][j-1] == '?'):
							l = i
							r = i
							while ((l >= 0) and (a[l][j] == orig)):
								l = l - 1
							while ((r < N) and (a[r][j] == orig)):
								r = r + 1
							flag = True
							for z in list(range(l+1, r)):
								if (a[z][j-1] != '?'):
									flag = False
							if flag:
								for z in list(range(l+1, r)):
									a[z][j-1] = orig
									cnt = cnt - 1

					if (i + 1 < N):
						if (a[i+1][j] == '?'):
							l = j
							r = j
							while ((l >= 0) and (a[i][l] == orig)):
								l = l - 1
							while ((r < M) and (a[i][r] == orig)):
								r = r + 1
							flag = True
							for z in list(range(l+1, r)):
								if (a[i+1][z] != '?'):
									flag = False
							if flag:
								for z in list(range(l+1, r)):
									a[i+1][z] = orig
									cnt = cnt - 1

					if (i - 1 >= 0):
						if (a[i-1][j] == '?'):
							l = j
							r = j
							while ((l >= 0) and (a[i][l] == orig)):
								l = l - 1
							while ((r < M) and (a[i][r] == orig)):
								r = r + 1
							flag = True
							for z in list(range(l+1, r)):
								if (a[i-1][z] != '?'):
									flag = False
							if flag:
								for z in list(range(l+1, r)):
									a[i-1][z] = orig
									cnt = cnt - 1

	print("Case #" + str(iT+1) + ":")
	for i in list(range(0, N)):
		for j in list(range(0, M)):
			print(a[i][j], end = '')
		print()
