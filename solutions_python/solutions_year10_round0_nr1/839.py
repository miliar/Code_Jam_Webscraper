n = int(raw_input())

for i in range(n):
	n, k = map(lambda x: int(x), raw_input().split(" "))
	print "Case #%d: "%(i+1),
	if k % (2 ** n) == (2 ** n) - 1:
		print "ON"
	else:
		print "OFF"
