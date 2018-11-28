import itertools

fd = open("in2.in", "r")

lines = fd.readlines()

testcases = int(lines[0])

fout = open("out2", "w")

def is_tidy(number):
	str_number = str(number)
	prev_i = 0
	for char in str_number:
		if(int(char) < prev_i):
			return False
		else:
			prev_i = int(char)
	return True

for line_ind in xrange(1,len(lines)):
	line  = lines[line_ind]
	fout.write("Case #" + str(line_ind) + ": ")
	maximum = int(line)
	# Your code here

	str_number = map(int, list(str(maximum)[::-1]))
	result = []
	for i in xrange(len(str_number)-1):
		if(str_number[i] < str_number[i+1]):
			result.append(9)
			result = map(lambda x: 9, result)
			str_number[i+1] -= 1
		else:
			result.append(str_number[i])
	result.append(str_number[-1])
	str_res = str(int("".join(map(str, result[::-1]))))
	print str_res
	fout.write(str_res + "\n")
