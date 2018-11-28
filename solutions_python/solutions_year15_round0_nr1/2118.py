import sys
input = sys.stdin

num_cases = int(input.readline())

for i in range(num_cases):
	input_tokens = input.readline().split(' ')
	s_max = int(input_tokens[0])
	audience = input_tokens[1]

	num_standing = 0
	num_needed = 0

	for shyness in range(s_max + 1):
		num_audience_this_shyness = int(audience[shyness])

		if num_standing < shyness:
			num_invite = shyness - num_standing
			num_needed += num_invite
			num_standing += num_invite

		num_standing += num_audience_this_shyness

	print 'Case #%d: %d' % (i + 1, num_needed)
	