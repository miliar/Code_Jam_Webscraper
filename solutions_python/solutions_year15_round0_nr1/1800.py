import sys

data = sys.stdin.readlines()
input_data = []
for line in data:
	line = line.rstrip()
	input_data.append(line)

count = 1
for string in input_data[1: len(input_data)]:
	string = string.split(' ')
	cur_str = string[1]
	cur_sum = 0
	cur_apl = 0
	for j in range(len(cur_str)):
		if cur_apl < j:
			cur_sum += j - cur_apl
			cur_apl += j - cur_apl
		cur_apl += int(cur_str[j])

	print "Case #" + str(count) + ": " + str(cur_sum)
	count += 1