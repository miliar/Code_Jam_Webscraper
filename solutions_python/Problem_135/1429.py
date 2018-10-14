import sys

f = open('input', 'r')

num_cases = int(f.readline().strip())
for cases in xrange(num_cases):
	row1 = int(f.readline().strip())
	for i in xrange(1,5):
		if i == row1:
			lst1 = f.readline().strip().split(" ")
			continue
		f.readline()

	row2 = int(f.readline().strip())
	for i in xrange(1,5):
		if i == row2:
			lst2 = f.readline().strip().split(" ")
			continue
		f.readline()
	intersect = list(set(lst1).intersection(lst2))

	if len(intersect) == 1:
		result =  intersect[0]
	elif len(intersect) > 1:
		result = "Bad magician!"
	else:
		result = "Volunteer cheated!"

	print "Case #" + str(cases+1) + ": " + result