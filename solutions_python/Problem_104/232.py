tst = int(input())
for t in range(1, tst+1):
	l = list(map(int, input().split()))

	print("Case #%d:" % t)

	for i in range(0, 3**l[0]):
		s1 = 0
		s2 = 0
		x = i
		for j in range(1, l[0] + 1):
			if x % 3 == 1:
				s1 += l[j]
			elif x % 3 == 2:
				s2 += l[j]
			x //= 3
			if x == 0: break
		if s1 == s2 and s1 != 0:
			x = i
			for j in range(1, l[0] + 1):
				if x % 3 == 1:
					 print(l[j], end=' ')
				x //= 3
				if x == 0: break
			print()
			x = i
			for j in range(1, l[0] + 1):
				if x % 3 == 2:
					 print(l[j], end=' ')
				x //= 3
				if x == 0: break;
			print()
			break
