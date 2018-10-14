import sys

def getLR(n):
	# print ("getting LR", n)
	if (n <= 0):
		return (0, 0)
	if (n % 2):
		l_val = n/2
		r_val = n/2
	else:
		l_val = n/2 - 1
		r_val = n/2
	return (l_val, r_val)

t = int(raw_input().strip())
for cnt in range(t):
	n, k = raw_input().strip().split(" ")
	n = int(n)
	k = int (k)
	if (n == k):
		print ("Case #{}: {} {}".format(cnt + 1, 0, 0))
	else:
		prev_big, prev_sml = 1, 0
		tom = k
		exp = 1
		while (tom > 1):
			exp *= 2
			tom /= 2
		# print (exp)
		k -= exp
		# print (k)
		x = 1
		while (x < exp):
			val = n / x
			if (val % 2) == 0:
				big = small = prev_big
				small += prev_sml * 2
			else:
				big = small = prev_sml
				big += 2 * prev_big
			prev_big = big
			prev_sml = small
			x *= 2
		# k = k - exp
		# print (n, exp, k, prev_big, prev_sml)
		prev_big -= k
		if (prev_big > 0):
			# tom = n / exp
			current = getLR(n / exp)
		else:
			# tom = n / exp - 1
			current = getLR((n / exp - 1))
		# print ("Case #{}: {} {} ({})".format(cnt + 1, max(current), min(current), tom))
		print ("Case #{}: {} {}".format(cnt + 1, max(current), min(current)))

