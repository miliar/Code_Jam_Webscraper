T = int(input())

for t in range(1, T + 1):

	[X, R, C] = input().split()
	X = int(X)
	R = int(R)
	C = int(C)

	lost = 0

	# Check for inherent spillage
	if ((R * C) % X != 0):
		lost = 1
	elif (X > C & X > R):
		lost = 1
	# Check for loss inducing blocks
	elif ((min(R, C) == 1) & (X >= 3)):
		lost = 1
	elif ((min(R,C) == 2) & (X >= 4)):
		lost = 1
	elif ((min(R,C) == 3) & (X >= 6)):
		lost = 1
	elif (X >= 7):
		lost = 1

	sol = "RICHARD" if lost else "GABRIEL"
	print("Case #{}: {}".format(t, sol))