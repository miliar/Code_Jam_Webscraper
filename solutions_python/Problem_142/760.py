import sys

def main(input_file):
	number_of_cases = int(input_file.readline().strip("\n"))
	for case_number in xrange(1, number_of_cases + 1):
		print "Case #%d: %s" % (case_number, case(input_file, case_number))

def case(input_file, case_number):
	n = int(input_file.readline().strip("\n"))
	words = []
	for i in xrange(n):
		words.append(input_file.readline().strip("\n"))
	word = words[0]
	base_word_list = []
	count_list = []
	
	last_c = ''
	count_list.append([])
	for c in word:
		if c != last_c:
			last_c = c
			base_word_list.append(last_c)
			count_list[-1].append(1)
		else:
			count_list[-1][-1] += 1
	base_word_len = len(base_word_list)

	for word in words[1:]:
		last_c = ''
		count_list.append([])
		i = 0
		for c in word:
			if c != last_c:
				last_c = c
				if i >= base_word_len or base_word_list[i] != c:
					return "Fegla Won"
				count_list[-1].append(1)
				i += 1
			else:
				count_list[-1][-1] += 1
		if i != base_word_len:
			return "Fegla Won"
	x = 0
	for i in xrange(base_word_len):
		x += abs(count_list[0][i] - count_list[1][i])
	return "%d" % (x, )
			
		
	

if __name__ == '__main__':
	main(open(sys.argv[1]))


