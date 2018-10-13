import sys

def find_char(line, line_index, magic_index):
    magic_str = "welcome to code jam"

    found = 0
    new_index = line.find(magic_str[magic_index], line_index)
    while new_index != -1:
        if magic_index == 18:
            found += 1
        else:
            found += find_char(line, new_index+1, magic_index+1)
        if found > 10000:
            found -= 10000
        # search from the next character after the one we found
        new_index += 1
        new_index = line.find(magic_str[magic_index], new_index)

    return found


#####################
# Main code
#####################
num_tests = int(sys.stdin.readline())

for ii in range(num_tests):
    line = sys.stdin.readline()

    line_index = 0
    magic_index = 0

    matches = find_char(line, line_index, magic_index)

    print("Case #" + str(ii+1) + ": {0:0=4}".format(matches))
