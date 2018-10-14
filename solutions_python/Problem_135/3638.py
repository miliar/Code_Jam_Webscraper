fo = open("A-small-attempt1.in", "r+")

T = 0

T = int(fo.readline())

for i in range(T):

	l1 = int(fo.readline())

	r1 = map(lambda v: int(v), fo.readline().split(" "))
	r2 = map(lambda v: int(v), fo.readline().split(" "))
	r3 = map(lambda v: int(v), fo.readline().split(" "))
	r4 = map(lambda v: int(v), fo.readline().split(" "))

	m1 = [r1, r2, r3, r4]

	l2 = int(fo.readline())

	r5 = map(lambda v: int(v), fo.readline().split(" "))
	r6 = map(lambda v: int(v), fo.readline().split(" "))
	r7 = map(lambda v: int(v), fo.readline().split(" "))
	r8 = map(lambda v: int(v), fo.readline().split(" "))

	m2 = [r5, r6, r7, r8]

	intersect = [val for val in m2[l2 - 1] if val in m1[l1 - 1]]

	result = ""

	if len(intersect) == 1:
		result = str(intersect[0])
	elif len(intersect) == 0:
		result = "Volunteer cheated!"
	else:
		result = "Bad magician!"

	print "Case #%d: %s" % (i + 1, result)