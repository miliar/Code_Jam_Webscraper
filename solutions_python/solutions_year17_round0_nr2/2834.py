t = int(raw_input())

def find_tidy(n):
	if n == "0":
		return ""

	digits = 1
	for j in xrange(len(n) - 1):
		if n[j] <= n[j + 1]:
			digits = digits + 1
		else:
			break

	if digits == len(n):
		return n
	else:
		front = int(n[0:digits]) - 1
		back = "9" * (len(n) - digits)
		return find_tidy(str(front)) + str(back)

for i in xrange(t):
	n = raw_input()
	print "Case #{}: {}".format(i+1, find_tidy(n))
