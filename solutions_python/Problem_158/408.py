import sys

def solve(x,r,c): # Assume we are richard as we are selecting the piece first
	lose = "GABRIEL" # No winning choises
	win = "RICHARD" # At least one winning choise
	
	# We can construct a 1xX line which can't be placed in the grid
	if x > max(r, c):
		return win

	# Impossible to fully cover the grid
	if (r * c) % x != 0:
		return win

	# We can construct a horizontal shape that would not fit
	if (x + 1) // 2 > min(r, c):
		return win

	# We can construct a hollow cube which will never be filled
	if x >= 7:
		return win

	if x == 6:
		if min(r, c) == 3:
			return win

	if x == 4:
		if min(r, c) == 2:
			return win

	# Grid will always be filled fully (assuming other rules are checked before)
	#if x == 1 or x == 2 or x == 3 or x == 5:
	return lose


f = open(sys.argv[1])
t = int(f.readline())

for _t in range(t):
	vals = f.readline().split()
	vals = [int(vals[i]) for i in range(len(vals))]
	
	print("Case #%d: %s" % (_t+1, solve(vals[0], vals[1], vals[2])))