number_cases = int(raw_input())

# h is always bigger than w
def dims_worst_piece(x):
	if x % 2:
		return (x/2, x/2 + 1)
	return ((x + 1)/2, (x + 1)/ 2)

def can_fill_small(x, r, c):
	if x == 1:
		return True
	if (r * c) % x:
		return False
	if x == 2:
		return True
	if r * c == x:
		return False
	if x == 3:
		return True
	if r <= 2 or c <= 2:
		return False
	return True

def can_fill(x, r, c):
	if r * c == x and x > 2:
		return False
	if (r * c) % x:
		return False
	if x > max(r, c):
		return False
	if x >= 7:
		return False
	w, h = dims_worst_piece(x)
	if w > min(r, c) or h > max(r, c):
		return False
	if x <= 3:
		return True
	#small case only
	if r <= 2 or c <= 2:
		return False
	return True

for n_case in xrange(number_cases):
	x, r, c = [int(x) for x in raw_input().split()]
	if can_fill_small(x, r, c):
		print "Case #{}: GABRIEL".format(n_case+1)
	else:
		print "Case #{}: RICHARD".format(n_case+1)