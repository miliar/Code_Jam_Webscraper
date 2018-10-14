def last_tidy(N):
	# N is str
	last = 1
	for j in range(len(N)):
		if int(N[j]) < last:
			res = str(int(N) - (int(N) % 10**(len(N)-j)) - 1)
			return last_tidy(res)
		last = int(N[j])
	return N

T = int(input())
for j in range(T):
	(N,) = input().split(" ")
	res = last_tidy(N)
	def check_tidy(N):
		N = str(N)
		for k in range(len(N)-1):
			if not int(N[k]) <= int(N[k+1]):
				return False
		return True
	assert check_tidy(res)
	assert not check_tidy(int(res) + 1) or int(res) == int(N)
	assert int(res) <= int(N)
	print("Case #%d: %s" % (j+1, res))
