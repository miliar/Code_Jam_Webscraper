cases = int(input())
for c in range(cases):
	s_max, l = input().split()
	s_max = int(s_max)
	l = [int(x) for x in l]
	
	friends = 0
	pos = 0
	for i in range(s_max + 1):
		for j in range(l[i]):
			if i > pos:
				friends += i - pos
				pos += i - pos
			pos += 1
	print("Case #{0}: {1}".format(c + 1, friends))