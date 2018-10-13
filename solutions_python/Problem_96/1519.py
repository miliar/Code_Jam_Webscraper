import string
import sys


def best_high_enough(score, p):
	#Simple Case
	if score < p : return 0
	
	base = score // 3
	diff = score % 3
	if (diff == 0) and (base >= p): return 1
	if (diff == 0) and ((base + 1) >= p): return -1
	if (diff == 1) and ((base + 1) >= p): return 1
	if (diff == 2) and ((base + 1) >= p): return 1
	if (diff == 2) and ((base + 2) >= p): return -1
	if (diff == 3) and ((base + 2) >= p): return -1	

	return 0

def calculate(line):
	line = line.split(None, 3)

	N = int(line[0])
	S = int(line[1])
	p = int(line[2])
	scores = line[3]

	high_enough = 0

	scores = scores.split()

	for score in scores:
		ret = best_high_enough(int(score), p)
		if ret == 1: high_enough += 1
		if ret == -1:
			if S > 0:
				S -= 1
				high_enough += 1

	return string.join([str(high_enough), '\n'],'')

#Standard CodeJam input munching
def codejam(fun):
	lines = sys.stdin.readlines()
	numlines = int(lines[0])

	for i in xrange(1,numlines+1):
		ans = string.join(["Case #", str(i), ": ", fun(lines[i])],'')
		sys.stdout.write(ans)

codejam(calculate) #ADD FUNCTION CALL HERE
