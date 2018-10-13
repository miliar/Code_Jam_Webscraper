import sys

def main() :
	lines = sys.stdin.readlines()
	cases = int(lines[0])
	for case in xrange(1,cases+1) :
		position = [1,1]; lastTime = [0,0];
		line = lines[case].split()
		seqLen = int(line[0])
		for i in xrange(seqLen) :
			color, pos = line[2*i+1], int(line[2*i+2])
			if color == 'O' :
				lastTime[0] = max(lastTime[1] + 1, lastTime[0] + abs(pos - position[0]) + 1)
				position[0] = pos
			elif color == 'B' :
				lastTime[1] = max(lastTime[0] + 1, lastTime[1] + abs(pos - position[1]) + 1)
				position[1] = pos
		print "Case #" + str(case) + ":" , max(lastTime[0],lastTime[1])

main()
