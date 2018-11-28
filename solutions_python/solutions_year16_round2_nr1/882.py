def counts(S):
	return tuple(sum(1 for c in S if ord(c) == ord('A') + i) for i in xrange(26))

tpl = [
	counts("ZERO"),
	counts("ONE"),
	counts("TWO"),
	counts("THREE"),
	counts("FOUR"),
	counts("FIVE"),
	counts("SIX"),
	counts("SEVEN"),
	counts("EIGHT"),
	counts("NINE")]

def matches(cn,digit):
	ret = list(cn)
	for i in xrange(26):
		if ret[i] >= tpl[digit][i]:
			ret[i] -= tpl[digit][i]
		else:
			return (None,False)

	return (tuple(ret),True)

def idx(c):
	return ord(c) - ord('A')

def solve(S):
	def rec(cn, seen):
		while cn[idx("Z")] > 0:
			(cn,ok) = matches(cn,0)
			assert ok
			seen += (0,)

		while cn[idx("G")] > 0:
			(cn,ok) = matches(cn,8)
			assert ok
			seen += (8,)

		while cn[idx("U")] > 0:
			(cn,ok) = matches(cn,4)
			assert ok
			seen += (4,)

		while cn[idx("X")] > 0:
			(cn,ok) = matches(cn,6)
			assert ok
			seen += (6,)

		while cn[idx("W")] > 0:
			(cn,ok) = matches(cn,2)
			assert ok
			seen += (2,)

		if sum(cn) == 0:
			return seen

		for i in xrange(10):
			(cnp, ok) = matches(cn,i)
			if ok:
				ret = rec(cnp,seen + (i,))
				if ret is not None:
					return ret

		return None

	cn = counts(S)
	tmp = rec(cn,())
	return ''.join(map(str, sorted(tmp)))

if __name__ == '__main__':
	T = int(raw_input())
	for t in xrange(T):
		S = raw_input().strip()
		print "case #%d: %s" % (t+1,solve(S))
