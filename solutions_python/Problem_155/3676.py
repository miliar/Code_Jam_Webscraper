T = int(input())

for case in range(T):
	_, s = input().split()
	s = list(map(int, list(s)))
	needed = 0
	total = s[0]
	for i in range(1, len(s)):
		if s[i] > 0 and i > total:
			needed += i-total
			total += needed
		total+=s[i]
	print("Case #%s: %s" % (case+1, needed))


