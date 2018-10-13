import math
T = input()
for t in range(1,T+1):
	A, B = map(int, raw_input().split())
	a, b = int(math.ceil(A**.5)), int(B**.5)
	n = 0
	for i in range(a, b+1):
		if str(i) == ''.join(reversed(str(i))):
			j = i*i
			if str(j) == ''.join(reversed(str(j))):
				n += 1
	print 'Case #' + str(t) + ':', n

	
