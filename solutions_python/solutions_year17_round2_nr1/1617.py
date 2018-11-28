input_f = "A-small-attempt0.in"

def process(horses, dest):
	times = [(dest-horses[0][0])/horses[0][1]]
	slowest_horse = 0
	for i in range(1, len(horses)):
		time = (dest-horses[i][0])/horses[i][1]
		times.append(time)
		if times[i] > times[i-1]:
			slowest_horse = i

	optimal_speed = dest/times[slowest_horse]
	print(horses, dest, slowest_horse, optimal_speed)
	return optimal_speed

lines = []
with open(input_f) as inf:
	with open(input_f+".out", "w") as out:
		test_cases = int(inf.readline())
		for t in range(test_cases):
			line = inf.readline()[:-1].split(" ")
			dest = int(line[0])
			num_of_horses = int(line[1])
			horses = []
			for h in range(num_of_horses):
				line = inf.readline()[:-1]
				horses.append([int(i) for i in line.split(" ")])
			out.write("Case #"+str(t+1)+": "+str(process(horses, dest))+"\n")
	# for line in inf:
	# 	line = line[:-1]
	# 	lines.append([int(i) for i in line.split(" ")])

print(lines)