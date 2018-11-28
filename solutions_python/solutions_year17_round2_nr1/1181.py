import fileinput


def time_h(horse, dist):
	start, speed = horse
	return float(dist - float(start))/float(speed)

def slowest_horse(horses, dist):
	min_horse = horses[0]
	min_time = 0
	for horse in horses:
		t = time_h(horse, dist)
		if t > min_time:
			min_time = t
			min_horse = horse
	return min_time

lines = [line.rstrip('\n') for line in fileinput.input()]

n = int(lines[0])
idx = 1
all_horses = {}
all_data = {}
testcase = 0

while idx < len(lines):
	dist, num = tuple(lines[idx].split(" "))
	dist = float(dist)
	num = int(num)
	horses = []
	idx += 1
	for h in range(num):
		horses.append(tuple(lines[idx].split(" ")))
		idx+=1
	all_horses[testcase] = horses
	all_data[testcase] = tuple([dist, num])
	testcase+=1

for case in all_horses:
	# print(case)
	dist, num = all_data[case]
	horse_list = all_horses[case]
	slowest_time = slowest_horse(horse_list, dist)
	# print(slowest_time)
	speed = float(dist) / slowest_time
	print("Case #" + str(case + 1) + ": " + str(speed))

