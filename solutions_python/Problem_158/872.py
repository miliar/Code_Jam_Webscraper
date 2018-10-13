file = open('D-small-attempt2.in');
cases = file.readline();
cases = str.split(cases, '\n')[0];
cases = int(cases);

out = open('D-small.out', 'w');

for i in range(0, cases):
	line = file.readline();
	line = str.split(line, ' ');
	X = int(line[0]);
	R = int(line[1]);
	C = int(line[2]);

	# If X is large enough, Richard can choose one with a hole and always win
	if X >= 7:
		winner = 1;

	# Check whether X divides the total number of tiles
	elif R*C % X != 0:
		winner = 1;

	elif X == 1 or X == 2:
		winner = 2; 

	# Check whether Richard can pick a tile that won't fit in the grid
	elif X > max(R, C):
		winner = 1;

	elif int(X / 2) + 1 > min(R, C):
		winner = 1;

	else:
		winner = 2;

	if winner == 1:
		player = "RICHARD";

	elif winner == 2:
		player = "GABRIEL";

	else:
		player = "UNKOWN";

	out.write("Case #%d: %s\n" % (i+1, player));
	print(winner);
