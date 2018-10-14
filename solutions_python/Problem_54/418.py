C = int(raw_input())

for c in range(C):
	str = raw_input()
	sl = str.split(' ')
	n = int(sl[0])
	t = []
	for i in range(1, n + 1, 1):
		t.append(long(sl[i]))
		
	t.sort()
	
	T = abs(t[0] - t[1])
	for i in range(1, n - 1, 1):
		b = abs(t[i] - t[i+1])
		while b != 0:
			x = b;
			b = T % b;
			T = x;

	y = T
	while y < t[0]:
		y += T

	y -= t[0]

	print("Case #%d: %d" % (c+1, y))
