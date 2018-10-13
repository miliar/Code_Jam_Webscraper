input_file = 'C-large.in'
output_file = "c_large_out.txt"

input = open(input_file, 'r')
output = open(output_file, 'w')

# number of cases
t = int(input.readline())

def solve(input_line):
    count = 0
    (lower, upper) = input_line.split(' ')
    lower = int(lower)
    upper = int(upper)
    for n in range(lower, upper):
        flipped_list = []
        str_n = str(n)
        for i in range(1, len(str_n)):
            flipped = int(str_n[i:] + str_n[:i])
            if flipped <= upper and flipped > n:
                flipped_list.append(flipped)
        flipped_set = set(flipped_list)
        count += len(flipped_set)
    return count

for i in range(t):
    line = input.readline()
    count = solve(line)
    output_line = "Case #%s: %s\n" % (i+1, count)
    output.write(output_line)

input.close()
output.close()
