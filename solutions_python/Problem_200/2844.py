import sys

def solve(num_array):
    length = len(num_array)
    for i in xrange(length - 1):
        low_pos = length - i - 2
        high_pos = length - i - 1
        if num_array[low_pos] > num_array[high_pos]:
            num_array[low_pos] -= 1
            for j in xrange(length - high_pos):
                num_array[high_pos + j] = 9
    while num_array[0] == 0:
        del num_array[0]
    num_array_str = [str(x) for x in num_array]
    num_str = "".join(num_array_str)
    return num_str

input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests

i = 1
for line in stripped_input_lines[1:]:
    num_array_str = list(line)
    num_array = [int(x) for x in num_array_str]
    result = solve(num_array)
    print "Case #" + str(i) + ": " + str(result)
    i += 1
