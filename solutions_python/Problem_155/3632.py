import sys

def count_audience_levels(standing, offset, audience_levels):
	pop = 0
	for i in range(0, len(audience_levels)):
		level = int(audience_levels[i])
		if (i + offset) <= standing or level == 0:
			standing += level
			pop += 1
		else:
			break
	offset += pop	
	return audience_levels[pop:], offset, standing

with open(sys.argv[1]) as input_file:
	test_cases = int(input_file.readline())
	for i in range(0, test_cases):
		split = input_file.readline().split()
		max_shyness, audience_levels = split[0], split[1]
		standing = 0
		offset = 0
		add_count = 0
		new_audience, offset, standing = count_audience_levels(standing, offset, audience_levels)
		while (len(new_audience) > 0):
			add_count += offset - standing
			standing += add_count
			if ((int(new_audience[0]) + standing) > int(max_shyness)):
				break
			new_audience, offset, standing = count_audience_levels(standing, offset, new_audience)
		print "Case #%d: %d" % (i + 1, add_count) 
