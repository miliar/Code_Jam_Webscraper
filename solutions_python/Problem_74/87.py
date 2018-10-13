def testCase():
	orders = raw_input().split(" ")[1:]
	position = [1, 1]
	time = [0, 0]
	for robot, button in zip(orders[::2], orders[1::2]):
		robot = {"B":0, "O":1}[robot]
		other = 1 - robot
		button = int(button)
		time[robot] = max(time[other], time[robot] + abs(button - position[robot])) + 1
		position[robot] = button
	return max(time)

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		print "Case #%d: %d" % (i + 1, testCase())
