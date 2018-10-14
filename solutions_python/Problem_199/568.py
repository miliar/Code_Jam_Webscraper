
def solve(s, k):
	# print (s)
	# print (k)

	k = int(k)
	s = [1 if i=='+' else 0 for i in s]
	
	#print s
	num_flips = 0
	for i in range(len(s) - k + 1):
		if s[i] == 0:
			for j in range(i,i+k):
				s[j] ^= 1
			#print s
			num_flips += 1

	
	for i in s:
		if i == 0:
			return "IMPOSSIBLE"
	return str(num_flips)


def process_file(fname):
	f = open(fname, 'r')
	fo = open(fname + ".result", "w")

	lines = f.readlines()
	lines = [i.strip() for i in lines]

	num_samples = int(lines[0])
	lines = lines[1:]

	#print("there are: %i samples" % num_samples)
	#print("")

	case_num = 1
	for l in lines:
		result = solve(*l.split(' '))
		to_print = "Case #%i: %s\n" % (case_num, result)
		fo.write(to_print)
		case_num += 1

process_file('sample.txt')
process_file('A-small-attempt0.in')
process_file('A-large.in')