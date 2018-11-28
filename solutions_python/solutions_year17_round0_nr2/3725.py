import sys


def is_tidy(n):
	n_str = str(n)
	prev = int(n_str[0])
	for i in range(len(n_str)):
		num_i = int(n_str[i])
		if num_i < prev:
			return False, len(n_str)-1 if int(n_str[-1]) == 0 else i
		prev = num_i
	return True, -1


def find_next_tidy(n):
    while True:
        tidy, wrong_index = is_tidy(n)
        if tidy:
            return n
        n_str = str(n)
        wrong_part = int(n_str[wrong_index:])
        n -= (wrong_part + 1)


if len(sys.argv) != 3:
    print("Use: {} <input_file> <output_file>".format(sys.argv[0]))
    exit(1)

input_filename, output_filename = sys.argv[1], sys.argv[2]
in_file = open(input_filename, 'r')
out_file = open(output_filename, 'w')
test_cases = int(in_file.readline())
for i in range(test_cases):
	num = int(in_file.readline())
	out_file.write("Case #{}: {}\n".format(i+1, find_next_tidy(num)))
in_file.close()
out_file.close()
