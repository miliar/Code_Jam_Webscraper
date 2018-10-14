import itertools

fd = open("in1.in", "r")

lines = fd.readlines()

testcases = int(lines[0])

fout = open("out1", "w")

line_ind = 1
case = 1
while line_ind < len(lines):
	line  = lines[line_ind].rstrip()
	fout.write("Case #" + str(case) + ": ")

	words = line.split()
	total_kilos = int(words[0])
	total_horses = int(words[1])

	# print line
	horses = []
	for i in xrange(total_horses):
		h_line = lines[line_ind + i + 1].rstrip()
		horse_data = map(int, h_line.split())

		horses.append(horse_data)


	# print horses


	slowest_horse_ind = -1
	slowest_horse = -1
	for i in xrange(total_horses):
		time_left = float((total_kilos - horses[i][0])) / horses[i][1]
		if time_left > slowest_horse:
			slowest_horse_ind = i
			slowest_horse = time_left

	# print horses[slowest_horse_ind]

	speed = float(total_kilos)/ slowest_horse

	# print speed
	fout.write(str(speed) + "\n")






	line_ind += 1 + total_horses
	case +=1
	# Your code here