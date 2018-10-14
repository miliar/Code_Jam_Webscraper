import sys

def count(line):
	array = line.split(' ')
	length = len(array[1])
	people_count = 0
	needed = 0
	for x in range(0, length):
		if x > people_count:
			needed += (x - people_count)
			people_count += (x - people_count)
		people_count += int(array[1][x])
	return needed
	
test_case_count = 1
i = 0;
for line in sys.stdin:
	if i == 0:
		i = 1
		continue
	line = line.strip()
	if(len(line) == 0):
		continue
	print "Case #{0}: {1}".format(test_case_count, count(line))
	test_case_count += 1