input_file = open("D-small-attempt0.in")
output_file = open("out", "w")

T = int(input_file.readline().strip())
for t in range(T):
	X, R, C = map(int, input_file.readline().strip().split(" "))
	
	richard_wins = (R * C % X != 0) or ((X <= 6) and (R < X - 1 or C < X - 1))

	output_file.write("Case #{0}: {1}\n".format(t + 1, "RICHARD" if richard_wins else "GABRIEL"))