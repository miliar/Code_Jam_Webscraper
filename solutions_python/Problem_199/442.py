
def filp(pankake, start, size):
	pk = list(pankake)
	for i in range(start+1,start+1+size):
		if pk[i] == '-':
			pk[i] = '+'
		else:
			pk[i] = '-'
	return ''.join(pk)


def f(pankake, k):

	nb = 0
	id = len(pankake)-1

	while '-' in pankake:
		while pankake[id] == '+':
			id -= 1
		sid = id-k
		if sid < -1:
			return "IMPOSSIBLE" 
		else:
			pankake = filp(pankake, sid, k)
			nb += 1

	return nb


n = int(input())

for i in range(n):

	pankake,k = input().split()
	k = int(k)

	print('CASE #'+str(i+1)+': ' + str(f(pankake,k)))