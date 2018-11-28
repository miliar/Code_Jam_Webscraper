def check_all_true(a):
	for el in a:
		if not(el):
			return False
	return True

def flip(a, i, K):
	for j in xrange(i, i+K):
		a[j] = not(a[j])

def solve(a, K):
	cnt = 0
	for i in xrange(len(a)):
		if i > len(a) - K:
			if check_all_true(a[i:]):
				return cnt
			else:
				return -1
		elif a[i] == False:
			flip(a, i, K)
			cnt += 1
		else:
			pass

T = int(raw_input().strip())


for i in xrange(1, T+1):
	inp, sz = raw_input().strip().split()
	sz = int(sz)
	a = []
	for ch in inp:
		if ch == '+':
			a.append(True)
		else:
			a.append(False)
	ans = solve(a, sz)
	if ans == -1:
		print "Case #" + str(i) + ": IMPOSSIBLE"
	else:
		print "Case #" +str(i) +": " + str(ans)