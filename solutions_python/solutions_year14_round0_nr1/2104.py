
def answer(ans, n_ans):
	if n_ans == 0:
		return 'Volunteer cheated!'
	elif n_ans > 1:
		return 'Bad magician!'
	return ans

t = input()
for k in xrange(t):
	row = input()
	pot = [0 for i in xrange(17)]
	for i in xrange(4):
		for n in [int(j) for j in raw_input().split()]:
			if i + 1 == row:
				pot[n] = 1
	row = input()
	n_ans = 0
	ans = 0
	for i in xrange(4):
		for n in [int(j) for j in raw_input().split()]:
			if i + 1 == row:
				if pot[n] == 1:
					ans = n
					n_ans += 1
	print 'Case #{0}: {1}'.format(k + 1, answer(ans, n_ans))
