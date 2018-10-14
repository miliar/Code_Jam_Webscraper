
def makeTurn(turn):
	robots = { 'O': { 'pos': 1, 'time': 0 }, 'B': { 'pos': 1, 'time': 0 } }
	while turn:
		robot = turn.pop(0)
		next_pos = int(turn.pop(0))
		steps = abs(robots[robot]['pos'] - next_pos)
		robots[robot]['pos'] = next_pos
		robots[robot]['time'] = max(robots['B' if robot == 'O' else 'O']['time'], robots[robot]['time'] + steps) + 1
	return max(robots['O']['time'], robots['B']['time'])

def main():
	with open("input.txt") as f:
		f.readline() # skip number of turns
		i = 1
		for line in f:
			print "Case #%d: %d" % (i, makeTurn(line.split()[1:]))
			i += 1

if __name__ == "__main__":
	main()

