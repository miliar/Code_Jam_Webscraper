ROBOTS = ['O', 'B']

def find_dest(moves, robot):
	for i, (candidate_robot, button) in enumerate(moves):
		if robot == candidate_robot:
			return i, button
	return -1, -1

def solve_test_case(line):
	tokens = line.split(' ')
	N = int(tokens[0])
	moves = []
	for i in xrange(N):
		robot = tokens[2*i+1]
		button = int(tokens[2*i+2])
		moves.append((robot, button))
	position = {robot:1 for robot in ROBOTS}
	time = 0
	while moves:
		button_pushed = False # was a button pushed this turn
		for robot in ROBOTS:
			move_index, destination = find_dest(moves, robot)
			if move_index == -1: # robot has no more moves
				# print "%s: stayed at %i" % (robot, position[robot]) 
				continue # to next robot
			if destination == position[robot]:
				if move_index == 0 and not button_pushed: # this is the next thing to do
					button_pushed = True
					# print "%s: pushed %i" % (robot, position[robot])
				else:
					# print "%s: stayed at %i" % (robot, position[robot])
					pass #we wait one round
			else: # we need to move robot towards destination
				delta = destination - position[robot]
				position[robot] += delta/abs(delta)
				# print "%s: moved to button %i" % (robot, position[robot])
		if button_pushed:
			moves = moves[1:]
		time += 1

	return time

def solve(filename):
	infile = open(filename, 'rb')
	T = infile.readline()
	for i in xrange(int(T)):
		result = solve_test_case(infile.readline().rstrip())
		print "Case #%d: %d" % (i+1, result)

if __name__ == "__main__":
	import sys
	solve(sys.argv[1])