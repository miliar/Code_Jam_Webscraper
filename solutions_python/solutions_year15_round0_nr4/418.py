def valid(x,r,c):
	area = r *c
	if area % x != 0:
		return False
	if r < x and c < x:
		return False
	if x == 1 or x == 2:
		return True
	if r == 1 or c == 1:
		return False
	if x == 3:
		return True
	if r == 2 or c == 2:
		return False
	return True

with open('D-small-attempt0.in') as f:
	with open('D-small-attempt0.out','w') as of:
		t = int(f.readline())
		for case_num in range(t):
			[x,r,c] = [int(x) for x in f.readline().split(" ")]
			if valid(x,r,c):
				of.write("Case #{}: GABRIEL\n".format(case_num + 1))
			else:
				of.write("Case #{}: RICHARD\n".format(case_num + 1))