import sys

def tidy(n):
	all_same = n[0] * len(n)
	all_same_int = int(''.join(all_same))

	# Return if valid already
	if is_valid(n):
		return n
	
	if all_same_int < int(n):
		# go up
		c = all_same_int
		i = c
		while i < int(n):
			if is_valid(i):
				c = i
			i += 1
		return c
	else:
		x = [int(x) for x in n]
		xi = x.index(min(x))
		for i in range (xi, len(x)):
			x[i] = x[xi]
		new = ''.join(map(str, x))
		if int(new) == int(n):
			return tidy(str(int(new) - 1))
		else:
			return tidy(new)
		
def is_valid(n):
	"""check to see if n is a tidy number."""
	if type(n) == int:
		n = str(n)
	for index, c in enumerate(n):
		if index == 0:
			continue
		if n[index - 1] > n[index]:
			return False
	return True

# read
for index, line in enumerate(sys.stdin):
	if index == 0:
		continue
	print("Case #%d: %s" % (index, tidy(line.rstrip())))

