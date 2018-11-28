import sys, operator, itertools

def str_to_bits(val):
	out = 0
	for x in val:
		if x == '0':
			out += 0
		else:
			out +=1
		out = out << 1
	return out

def main(argv):
	file_name = argv[0]
	f = open(file_name, 'r')
	number_tests = int(f.readline())

	for count in range(number_tests):
		first_line = f.readline()
		first_line = first_line.split()
		first_line = map(int, first_line)

		i = 0

		for a in range(first_line[0]):
			for b in range(first_line[1]):
				if first_line[2] > a & b:
					i += 1
					

		print "Case #" + str(count+1) + ": " + str(i)

if __name__ == "__main__":
   main(sys.argv[1:])
