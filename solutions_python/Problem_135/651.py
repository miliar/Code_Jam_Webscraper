from sets import Set

data = open("small_set.txt").readlines()
length = (len(data) - 1) / 10

answer1_offset = 1
answer2_offset = 6

for entry in xrange(length):
	answer1 = int(data[(entry * 10) + answer1_offset])
	answer2 = int(data[(entry * 10) + answer2_offset])
	
	row1 = data[(entry * 10) + answer1 + answer1_offset]
	row2 = data[(entry * 10) + answer2 + answer2_offset]

	row1 = Set(row1.split())
	row2 = Set(row2.split())

	#row1 = Set([int(x) for x in row1.split()])
	#row2 = Set([int(x) for x in row2.split()])

	possible = row1 & row2
	if len(possible) == 1:
		out = possible.pop()
	elif len(possible) == 0:
		out = "Volunteer cheated!"
	elif len(possible) > 1:
		out = "Bad magician!"

	print "Case #%i: %s" % (entry + 1, out)
