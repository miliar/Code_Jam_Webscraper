def solve(N):
	cur = 0
	cnt = 0
	res = '0'
	length = len(N)
	for i in range(length):
		n = int(N[i])
		if cur <= n:
			if cur == n: cnt += 1
			else: cnt = 0
			res += str(n)
			cur = n
		else:
			res = res[:(i - cnt)] + str(cur - 1)
			res += '9' * (length - i + cnt)
			break
	return str(int(res))

f = open(‘B.txt’, ‘w’)
for _ in range(int(input())):
	f.write('Case #' + str(_ + 1) + ': ' + solve(input()))
f.close()
