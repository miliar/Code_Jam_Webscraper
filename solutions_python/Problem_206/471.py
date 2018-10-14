t = int(raw_input())

answers = []
for test in range(0, t):
	in_str = raw_input()
	distance = float(in_str.split(' ')[0])
	horses = int(in_str.split(' ')[1])
	starts = []
	speeds = []
	for i in range(0, horses):
		in_str = raw_input()
		starts.append(float(in_str.split(' ')[0]))
		speeds.append(float(in_str.split(' ')[1]))

	longest_time = 0
	for i in range(0, horses):
		time = (distance - starts[i]) / speeds[i]
		longest_time = max(time, longest_time)

	answers.append(distance / longest_time)

for test in range(0, t):
	out_str = "Case #" + str(test+1) + ": " + str(answers[test])

	print out_str