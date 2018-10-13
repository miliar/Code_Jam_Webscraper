def candies(C):
	for n in range(1, int('1'*len(C), 2)):
		s = bin(n)[2:]
		s = ('0'*(len(C)-len(s))) + s
		mask = map(lambda x: bool(int(x)), reversed(s))
		pat, pat2, sean = 0, 0, 0
		for (topat, c) in zip(mask, C):
			if topat:
				pat ^= c
			else:
				pat2 ^= c # pat count of the other pile
				sean += c
		if pat == pat2:
			return sean
	return 'NO'

T = int(input().rstrip())
for x in range(1, T+1):
	N = int(input().rstrip())
	C = list(map(int, input().rstrip().split(' ')))
	C.sort()
	print('Case #{}: {}'.format(x, candies(C)))
