T = int(input())

for t in range(T):
	N = int(input())
	res = 0
	#print(N)
	tab = list(map(int, list(str(N))))
	#print(tab)

	s = ''
	for i in range(len(tab)):
		idx = len(tab)-i-1
		#print(idx)
		#print(tab)
		if idx == 0:
			s = str(tab[idx]) + s
		else:
			if tab[idx] >= tab[idx-1] and tab[idx] != 0:
				s = str(tab[idx]) + s
			else:
				tab[idx] = 9
				s = str(tab[idx]) + ''.join(['9'] * len(s))

				idx -= 1
				while idx >= 0:
					if tab[idx] > 0:
						tab[idx] -= 1
						break
					else:
						tab[idx] = 9

					idx -= 1


	#print(tab)
	#print(s)

	print("Case #{}: {}".format(t+1, s.lstrip('0')))