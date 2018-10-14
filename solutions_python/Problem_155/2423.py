input_file = open('A-large.in', 'r')
output_file = open('output.txt', 'w')
test_cases = int(input_file.readline())

for _ in xrange(test_cases):
	standing_audience, extra_friends = 0, 0
	shyness_max, shyness_list = input_file.readline().split(' ')
	for shyness in xrange(int(shyness_max) + 1):
		if shyness_list[shyness] > '0' and standing_audience < shyness:
			extra_friends += (shyness - standing_audience)
			standing_audience = shyness
		standing_audience += int(shyness_list[shyness])
	output_file.write("Case #%d: %d" %( _+1, extra_friends))
	output_file.write("\n");

input_file.close()
output_file.close()