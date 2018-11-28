import math

infile = open('in.in', 'r');
outfile = open('out', 'w');

num_input = int(infile.readline());

for i in range(num_input):
	test_range = infile.readline();
	test_range = test_range.split(' ');
	range_start = int(test_range[0]);
	range_start = int(math.ceil(math.sqrt(range_start)));
	range_end = int(test_range[1]);
	range_end = int(math.floor(math.sqrt(range_end)));

	fair_square = 0;
	for x in range(range_start, range_end + 1):
		x_reverse = int("".join(reversed(list(str(x)))));
		x_square = x ** 2;
		x_square_reverse = int("".join(reversed(list(str(x_square)))));
		if x == x_reverse and x_square == x_square_reverse:
			fair_square += 1;

	outfile.write('Case #' + str(i + 1) + ': ');
	outfile.write(str(fair_square));
	outfile.write('\n');