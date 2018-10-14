def is_tidy(n):
	if n < 10:
		return True
	u = n % 10
	d = (n /10) % 10
	return is_tidy(n / 10) and d <= u


#print is_tidy(23)
#print is_tidy(223)
#print is_tidy(233238693423948711)

def max_tidy_lt(n):
	while not is_tidy(n):
		n -= 1
	return n

#print max_tidy_lt(132)
#print max_tidy_lt(1000)
#print max_tidy_lt(7)

with open('B-small-attempt0.in', 'r') as file:
	lines = file.readlines()
	print lines[0]
	for i in range(1, len(lines)):
		print 'Case #{}: {}'.format(i, max_tidy_lt(int(lines[i].strip())))