import math
t = int(raw_input())

mins = []
maxes = []
for i in range(0, t):
	in_str = raw_input()
	stalls = int(in_str.split(" ")[0])
	people = int(in_str.split(" ")[1])

	divisor = pow(2, int(math.log(people, 2)))
	stalls -= (people - divisor)
	current_section = (stalls / divisor)
	latest_max = current_section / 2
	latest_min = latest_max
	if current_section % 2 == 0:
		latest_min -= 1

	mins.append(latest_min)
	maxes.append(latest_max)

for i in range(0, t):
	out_str = "Case #" + str(i+1) + ": "
	out_str += str(maxes[i]) + " " + str(mins[i])
	print out_str