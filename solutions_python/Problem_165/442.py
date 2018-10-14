def F(r, c, w):
	if c == w:
		return w
	
	if c+1 == w:
		return w

	if w*2 > c:
		 return w+1

	return 1 + F(r, c-w, w)


N = int(raw_input())

for test in range(1, N+1):
	r, c, w = map(int, raw_input().split())

	answer = F(r, c ,w)

	print "Case #{}: {}".format(test, r * answer)

