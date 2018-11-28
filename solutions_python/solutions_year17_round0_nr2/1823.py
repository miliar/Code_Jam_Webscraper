def is_tidy(n):
	l = list(n)
	for i in range(len(l)):
		l[i] = int(l[i])
	_l = l[:]
	_l.sort()
	return (True if _l == l else False)

T = int(input())

N = []
for _ in range(T):
	N.append(input())

for cnt in range(T):
	print('Case #%d: '%(cnt+1), end='')

	if is_tidy(N[cnt]):
		print(N[cnt])
	else:
		while not is_tidy(N[cnt]):
			ind = 0
			n = list(N[cnt])
			for i in range(len(n)-1):
				if int(n[i]) > int(n[i+1]):
					ind = i
			n[ind] = str(int(n[ind])-1)
			for i in range(ind+1,len(n)):
				n[i] = '9'
			N[cnt] = ''.join(n)


		print(int(''.join(n)))