import sys


def is_tidy(N):
	st = str(N)
	for i in range(len(st)-1):
		if st[i] > st[i+1]:
			return False
	return True

def dec(N):
	st = str(N)
	l = len(st)
	k = -1
	last = st[k]
	cursor = 0
	rep = 0
	if last == '0':
		k-=1
		while st[k] == '0':
			k-=1
		if k == -l:
			return N-1
		cursor = st[k]
		while k > -l:
			k = k - 1
			e = st[k]
			if e == cursor:
				rep = rep + 1
			else:
				break
		if rep > 0:
			return N - (N % pow(10, rep+1))
		else:
			return N - 1
	else:
		return N-1

T = sys.stdin.readline().splitlines()[0]

for i in range(int(T)):
	N = int(sys.stdin.readline().splitlines()[0])
	res = N

	while res > 0:
		if is_tidy(res):
			break
		res = dec(res)

	print('Case #' + str(i+1) + ': ' + str(res))
