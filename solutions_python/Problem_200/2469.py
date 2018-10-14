def is_tidy(N):
	if 0 in N:
		return False
	else:
		return N == sorted(N)

def last_tidy(N, case_num):
	N = [int(x) for x in list(N)]
	tidy = [0]
	same = True
	if is_tidy(N):
		tidy = N
	else:
		m = max(N)
		idx = N.index(m)
		while N[: idx] != sorted(N[: idx]):
			m = max(N[: idx])
			idx = N.index(m)
			
		N[idx] -= 1
		for i in range(idx+1, len(N)):
			#if same and N[i] == m and m != 1:
				#print N[i], i
				#same = True
			#else:
			#	same = False
				N[i] = 9
	if 0 in N:
		N.remove(0)

	tidy = ''.join([str(x) for x in N])
	print "Case #{}: {}".format(case_num, tidy)



T = int(raw_input())  # read a line with a single integer
for case_num in xrange(1, T + 1):
  N = raw_input()
  last_tidy(N, case_num)
  # check out .format's specification for more formatting options