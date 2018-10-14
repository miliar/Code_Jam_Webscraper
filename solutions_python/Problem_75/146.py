import sys

input_file = sys.stdin
output_file = sys.stdout

t = int(input_file.readline().strip())

for i in range(t):
	line = input_file.readline().split()

	c = int(line[0])
	combine = []
	for j in range(c):
		combine.append(line[j + 1])

	d = int(line[c + 1])
	oppose = []
	for j in range(d):
		oppose.append(line[c + 2 + j])

	n = int(line[c + d + 2])
	input_seq = line[c + d + 3]

	seq = []
	for j in range(n):
		seq.append(input_seq[j])

		while True:
			if (1 < len(seq)):
				done = False
				for comb in combine:
					if ((comb[0] == seq[len(seq) - 1]) and (comb[1] == seq[len(seq) - 2])) or ((comb[0] == seq[len(seq) - 2]) and (comb[1] == seq[len(seq) - 1])):
						seq.pop()
						seq.pop()
						seq.append(comb[2])
						done = True
						break
				if done:
					continue

				for opp in oppose:
					if ((opp[0] == seq[len(seq) - 1]) and (opp[1] in seq)) or ((opp[1] == seq[len(seq) - 1]) and (opp[0] in seq)):
						seq = []
						done = True
						break
				if done:
					continue

			break
			
		
	output_file.write("Case #" + str(i + 1) + ": [" + ", ".join(seq) + "]\n")

