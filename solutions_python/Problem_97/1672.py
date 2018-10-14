def rot (a, b):
	a = str (a)
	b = str (b)
	for i in range (len (a)):
		if a == b:
			return True
		a = a[1:] + a[0]
	return False

T = int (input ())

for t in range (1, T + 1):
	l = input ()
	l = l.split (" ")
	A = int (l [0])
	B = int (l [1])
	cnt = 0
	for n in range (A, B + 1):
		for m in range (n + 1, B + 1):
			if rot (n, m):
				cnt += 1
	print ("Case #" + str (t) + ": " + str (cnt))