def solvedumb(hi,lo,lst):
	lst = map(int,lst.split(" "))
	for i in range(lo,hi+1):
		f = False
		for k in lst:
			if i % k != 0 and k % i != 0:
				f = True
				continue
		if not f:
			return i
	return False
