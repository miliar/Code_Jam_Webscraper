
def sign(x):
	if x > 0:
		return 1
	elif x < 0: 
		return -1
	else:
		return 0

def solve(sequence):
	last_robot = sequence[0][0]
	last_robot_time = 0
	time = 0
	pos = [1,1]
	for r,k in sequence:
		if last_robot != r:
			# account for the actions of the previous robot.
			pos[r] += min(last_robot_time, abs(k - pos[r])) * sign(k - pos[r])
			last_robot = r
			last_robot_time = 0

		# move to the correct place
		time += abs(k - pos[r])
		last_robot_time += abs(k - pos[r])
		pos[r] = k
		# click
		time += 1
		last_robot_time += 1
	
	return time


def gcj():
	f = open("data","r")
	T = int(f.readline())
	for i in range(1,T+1):
		# test case specifics
		test_case = f.readline().strip().split(' ')
		N = int(test_case[0])
		j = 1
		sequence = []
		while j < len(test_case) - 1:
			if test_case[j] == "O":
				robot = 0
			else:
				robot = 1
			sequence.append((robot, int(test_case[j+1])))
			j += 2
		sol = solve(sequence)
		# end test case specific
		print "Case #%d: %d" % (i, sol)
	f.close()

if __name__ == "__main__":
	gcj()





			
