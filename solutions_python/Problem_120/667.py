import math



# a = pi * (R1^2 - R2^2)


numCases = input()

for case in xrange(1, numCases + 1):
	(R1, paint) = [int(x) for x in raw_input().split(' ')]
	
	circles = 0

	while paint > 0:
		area = (R1+1)*(R1+1) - (R1)*(R1)
		# print area
		if paint - area >= 0:
			paint -= area
			circles += 1
			R1 += 2
		else:
			break
	print "Case #%d: %d" % (case, circles)

# Case #1: 1
# Case #2: 2
# Case #3: 3
# Case #4: 707106780
# Case #5: 49
