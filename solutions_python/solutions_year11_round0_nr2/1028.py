

def solve(seq,base,opposite):
	stack = []
	for ch in seq:
		stack.append(ch)
		if len(stack) < 2:
			continue
		if ch in base and stack[-2] == base[ch][0]:
			a = stack.pop()
			b = stack.pop()
			stack.append(base[ch][1])
			continue
		if ch in opposite and stack.count(opposite[ch]):
			stack = []

	return "[%s]" % ', '.join(stack)


def gcj():
	f = open("data","r")
	T = int(f.readline())
	for i in range(1,T+1):
		# test case specifics
		test_case = f.readline().strip().split(' ')
		C = int(test_case[0])
		test_case = test_case[1:]
		base = {}
		for j in range(0,C):
			s = test_case[0]
			test_case = test_case[1:]
			# FQT => base[F] = (Q,T), base[Q] = (F,T)
			base[s[0]] = (s[1],s[2])
			base[s[1]] = (s[0],s[2])

		D  = int(test_case[0])
		test_case = test_case[1:]
		opposite = {}
		for j in range(0,D):
			s = test_case[0]
			test_case = test_case[1:]
			opposite[s[0]] = s[1] # not present
			opposite[s[1]] = s[0] # not present
	
		N = int(test_case[0])
		seq = test_case[1]
		sol = solve(seq,base,opposite)
		
		print "Case #%d: %s" % (i, sol)
		# end test case specific
	f.close()

if __name__ == "__main__":
	gcj()





			
