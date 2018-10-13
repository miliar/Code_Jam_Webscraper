import sys

sys.stdin = open("B-large.in")

lines = [line.strip() for line in sys.stdin]

testCases = int(lines.pop(0))

curTest = 0

while curTest < testCases:
	cr = 2.0
	farmC, farmR, ct = map(float, lines[curTest].split())
	timespent = 0.0
	prevt = (ct / cr) + timespent
	time = (ct / cr) + timespent
	while prevt >= time:
		timespent += farmC / cr
		cr += farmR
		prevt = time
		time = (ct / cr) + timespent
	print "Case #" + str(curTest + 1) + ": " + ("{:10.7f}".format(prevt)).strip()
	curTest += 1
