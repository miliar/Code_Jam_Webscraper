import sys

input_file = open(sys.argv[1])
output_file = open(sys.argv[1] + ".out", "w")

T = int(input_file.readline().strip())
for t in range(1, T + 1):
	N = int(input_file.readline().strip())
	m = list(map(int, input_file.readline().strip().split(" ")))

	pieces_eaten_a = []
	for i in range(N - 1):
		pieces_eaten_a.append(max(0, m[i] - m[i + 1]))

	y = int(sum(pieces_eaten_a))

	rate = (max(pieces_eaten_a) / 10)

	pieces_eaten_b = []
	for i in range(N - 1):
		pieces_eaten_b.append(min(m[i], 10 * rate))

	z = int(sum(pieces_eaten_b))

	output_file.write("Case #{0}: {1} {2}\n".format(t, y, z))
