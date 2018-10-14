

def time_to_dest(D, I, S):
	return float(D - I) / S




with open("A-large.in", "r") as dataset:
	nb_cases = int(dataset.readline().rstrip("\n"))
	out = []
	for i in range(nb_cases):
		D, N = [int(x) for x in dataset.readline().rstrip("\n").split(' ')]
		times = []
		for j in range(N):
			I, S = [int(x) for x in dataset.readline().rstrip("\n").split(' ')]
			times.append(time_to_dest(D, I, S))
		times.sort()
		out.append("Case #" + str(i + 1) + ": " + str(float(D)/times.pop()))




with open("result.txt", "w+") as output_file:
		for line in out:
			output_file.write(line + "\n")