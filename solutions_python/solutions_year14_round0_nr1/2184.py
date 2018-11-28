import sys

lines = sys.stdin.readlines()

num_probs = int(lines[0])

for index in xrange(num_probs):

	row_id = int(lines[10*index+1])
	row_1 = {int(x) for x in lines[10*index + 1 + row_id].split()}

	row_id = int(lines[10*index+1 + 5])
	row_2 = {int(x) for x in lines[10*index + 1 + 5 + row_id].split()}

	common = row_1.intersection(row_2)
	num_common = len(common)

	res = "Case #%d: " % (index + 1)
	if num_common == 1:
		res = "%s%d" % (res, list(common)[0])
	elif num_common == 0:
		res = "%s%s" % (res, "Volunteer cheated!")
	else:
		res = "%s%s" % (res, "Bad magician!")

	print res