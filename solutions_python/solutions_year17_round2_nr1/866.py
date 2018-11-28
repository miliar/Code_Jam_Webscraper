from sys import argv, stdout

def solve(loc, horses):
	horses = [map(float, horse) for horse in horses]
	horse_time_to_finish = [(loc - starting) / speed for starting, speed in horses]
	max_speed_to_finish = loc / max(horse_time_to_finish)
	return str(max_speed_to_finish)

if __name__ == "__main__":
	infile = open(argv[1], 'r')
	T = int(infile.readline())
	for case in range(T):
		loc, num_horses = infile.readline().strip().split(' ')
		horses = []
		for h in range(int(num_horses)):
			horses.append(infile.readline().strip().split(' '))
		stdout.write("Case #%d: %s\n"  % (case+1, solve(int(loc), horses)))