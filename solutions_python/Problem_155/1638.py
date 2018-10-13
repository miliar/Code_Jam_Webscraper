file = open('A-large.in');
cases = file.readline();
cases = str.split(cases, '\n');
cases = int(cases[0]);
out = open('A-large.out', 'w');

for j in range(0, cases):

	line = file.readline();
	line = str.split(line, ' ');
	Smax = int(line[0]);
	line = str.split(line[1], '\n');
	audience = line[0];

	friends = 0;
	clapping = 0;

	for i in range(0, Smax + 1):
		if clapping < i:
			friends = friends + i - clapping;
			clapping = i;

		clapping = clapping + int(audience[i]);

	# Output
	out.write("Case #%d: %d\n" % (j+1, friends) );
	print("Case #%d: %d" % (j+1, friends) );
