# Google Code Jam 2015  Standing Ovation
import sys

lines = (line.rstrip() for line in sys.stdin.readlines())
t = int(lines.next())

for i in xrange(1, t + 1):
	(s_max, audience) = [x for x in lines.next().split()]
	s_max = int(s_max)
	guests = 0
	standing = 0
	for shyness in xrange(1, s_max + 1):
		standing += int(audience[shyness - 1]) 
		if (standing < shyness):
			diff = (shyness - standing)
			guests += diff
			standing += diff

	print "Case #%s: %s" % (i, guests)
