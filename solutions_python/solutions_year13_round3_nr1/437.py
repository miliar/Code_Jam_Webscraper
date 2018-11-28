def file_read(file):
	file_open = open(file, 'r')
	
	for line in file_open:
		yield line
	
	file_open.close()

input = file_read('A-small-attempt0.in')
output = open("A-small-attempt0.out","w")

T = int(input.next())

def find_vowel(str):
	for i in xrange(len(str)):
		s = str[i]
		if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
			return i
	return -1

for i in xrange(T):
	line1 = input.next().split()

	input_str = line1[0]
	n = int(line1[1])
	full_len = len(input_str)
	
	prev_start = 0
	start = 0
	
	solution = 0
	
	while len(input_str[start:]) >= n:
		sub_str = input_str[start:]
		vowel = find_vowel(sub_str)
		if vowel == -1 or vowel >= n:
			solution += (start + 1 - prev_start)*(len(sub_str) - n + 1)
			prev_start = start + 1
			start += 1
		else:
			start += vowel + 1
	
	
	
	output.write("Case #"+str(i+1)+": "+str(solution)+"\n")
	