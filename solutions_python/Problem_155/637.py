# read input
f = open("1_large.in");
lines = [l.strip() for l in f]

ncases = int(lines[0])

outfile = open("1.out", "w")
output_str = 'Case #{0}: {1}\n'

for i in range(1, ncases+1):
	input = lines[i].split()

	n_types = int(input[0]) + 1

	if n_types > 0:
		people = [int(x) for x in list(input[1])]

		n_to_add = max([k - sum(people[0:k]) for k in range(n_types + 1)])
	else:
		n_to_add = 0

	outfile.write(output_str.format(i, n_to_add))

outfile.close()