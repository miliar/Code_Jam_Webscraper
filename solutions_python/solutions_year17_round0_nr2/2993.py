import sys

def reset_to_9(str_num_list, starting_index):
    for i in range(starting_index, len(str_num_list)):
        str_num_list[i] = '9'
    return str_num_list

def last_tidy_number(num):
    str_num_list = list(str(num))
    i = len(str_num_list) - 1
    while i > 0:
        if str_num_list[i-1] > str_num_list[i]:
            str_num_list[i-1] = chr(ord(str_num_list[i-1]) - 1)
            str_num_list = reset_to_9(str_num_list, i)
        i -= 1
    return int(''.join(str_num_list))


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    for i in range(1, len(lines)):
        print "Case #{}: {}".format(i, last_tidy_number(int(lines[i])))

