import sys

sys.stdin = open('in.txt', 'r+')
sys.stdout = open('out.txt', 'w+')

def bigger(x): # 1324 -> 1334 // 3456 -> 3456
	r = ''
	b = '1'
	for i in range(len(x)):
		b = max(b, x[i])
		r += b 

	return r

TC = int(input())
for _ in xrange(1, TC+1):
	n = raw_input()
	res = ''

	if '1' * len(n) > n:
		res = '9' * max(len(n)-1, 1)
	else:
		L = '1' * len(n)
		R = '9' * len(n)

		while int(L)<=int(R):
			M = str((int(L) + int(R)) // 2)
			if bigger(M) <= n:
				L = str(int(M) + 1)
				res = bigger(M)
			else:
				R = str(int(M) - 1)

	print("Case #{0}: {1}".format(_, res))