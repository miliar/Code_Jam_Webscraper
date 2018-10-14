#No time for proper solution

input = open("D-small-attempt2.in", "r")
output = open("result.out", "w")

T = int(input.readline())
case = 0
for line in input:
	case += 1
	(X, R, C) = list(map(int, line.split()))
	if X == 1:
		output.write("Case #{}: GABRIEL\n".format(case, 0))
	elif X == 2:
		if (R * C) % 2 == 0:
			output.write("Case #{}: GABRIEL\n".format(case, 0))
		else:
			output.write("Case #{}: RICHARD\n".format(case, 0))
	elif X == 3:
		if (R * C) % 3 == 0 and (R > 1 and C > 1):
			output.write("Case #{}: GABRIEL\n".format(case, 0))
		else:
			output.write("Case #{}: RICHARD\n".format(case, 0))
	elif X == 4:
		if (R * C) >= 12:
			output.write("Case #{}: GABRIEL\n".format(case, 0))
		else:
			output.write("Case #{}: RICHARD\n".format(case, 0))
	else:
		output.write("Case #{}: DEFAULT\n".format(case, 0))
		print("Case", case, ": default")

input.close()
output.close()