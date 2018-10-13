# coding=utf-8
from math import sqrt


def read_input(file_name):
    with open(file_name, 'r') as f:
        input_data = f.read()
    lines = input_data.split()
    num_cases = int(lines.pop(0))
    range_list = lines
    return num_cases, range_list


def is_pal(num_str):
    if num_str == num_str[::-1]:
        return True
    else:
        return False


def is_fair_square(num):
    sq_num = sqrt(num)
    if sq_num.is_integer() and sq_num ** 2 == num and is_pal(str(num)) and is_pal(str(int(sq_num))):
        return True
    else:
        return False


def main():
    num_cases, range_list = read_input('C-small-attempt0.in')
    out_file = open('C-small-attempt0.out', 'w')
    for c in range(num_cases):
        fair_count = 0
        for i in range(int(range_list[c * 2]), int(range_list[c * 2 + 1]) + 1):
            if is_fair_square(i):
                fair_count += 1
        out_file.write("Case #%d: %d\n" % (c + 1, fair_count))
        print("Case #%d: %d" % (c + 1, fair_count))
    out_file.close()


if __name__ == '__main__':
    main()