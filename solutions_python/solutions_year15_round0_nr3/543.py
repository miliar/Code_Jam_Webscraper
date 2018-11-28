import re


def split_sign(a):
    if a == "":
        return "", 1
    elif a[0] == "-":
        return a[1:], -1
    else:
        return a, 1


def join_sign(num, sign):
    return ("-" if (sign == -1) else "") + str(num)


def multiply(a, b):
    (abs_a, sign_a) = split_sign(a)
    (abs_b, sign_b) = split_sign(b)
    abs_result = ''
    sign_result = 1

    if abs_a == '':
        abs_result = abs_b
        sign_result = 1
    if abs_b == '':
        abs_result = abs_a
        sign_result = 1
    elif abs_a == 'i':
        if abs_b == 'j':
            abs_result = 'k'
            sign_result = 1
        elif abs_b == 'k':
            abs_result = 'j'
            sign_result = -1
        elif abs_b == 'i':
            abs_result = ''
            sign_result = -1
    elif abs_a == 'j':
        if abs_b == 'j':
            abs_result = ''
            sign_result = -1
        elif abs_b == 'k':
            abs_result = 'i'
            sign_result = 1
        elif abs_b == 'i':
            abs_result = 'k'
            sign_result = -1
    elif abs_a == 'k':
        if abs_b == 'j':
            abs_result = 'i'
            sign_result = -1
        elif abs_b == 'k':
            abs_result = ''
            sign_result = -1
        elif abs_b == 'i':
            abs_result = 'j'
            sign_result = 1
    return join_sign(abs_result, (sign_a * sign_b * sign_result))


test_count = input()


def get_long_digit(the_line, the_index):
    return the_line[the_index % len(the_line)]


def evaluate(line):
    result = ""
    for the_index in range(0, len(line)):
        result = multiply(result, line[the_index])
    return result


def power(value, n):
    if n == 0:
        return ""
    if n == 1:
        return value
    if n % 2 == 0:
        return power(multiply(value, value), n/2)
    else:
        return multiply(value, power(value, n - 1))

def multiply_long_range(line, start, stop):
    line_len = len(line)
    # if they're in the same segment
    if (start / line_len == stop / line_len):
        result = ""
        # print "RANGE " + str(start) + " " + str(stop + 1)
        for the_index in range(start, stop + 1):
            result = multiply(result, get_long_digit(line, the_index))
        return result

    # not in same segment
    first_segment_result = ""
    for the_index in range(start, start + (line_len - start % line_len)):
        first_segment_result = multiply(first_segment_result, get_long_digit(line, the_index))

    # any middle segments?
    middle_segments = ""
    if start + (line_len - start % line_len) < stop - (stop % line_len):
        num_of_segments = ((stop - (stop % line_len)) - (start + (line_len - start % line_len)))/line_len
        middle_segments = power(evaluate(line), num_of_segments)

    last_segment = ""
    for the_index in range(stop - (stop % line_len), stop + 1):
        last_segment = multiply(last_segment, get_long_digit(line, the_index))
    return multiply(first_segment_result, multiply(middle_segments, last_segment))

for i in range(0, test_count):
    succeed = False
    line = raw_input()
    groups = re.search("(\d+) (\d+)", line)
    l = int(groups.group(1))
    x = int(groups.group(2))

    # for a very long string, try searching for an i near the beginning and a k near the end
    # then multiply out the remaining middle digits and look for a j

    line = raw_input().rstrip()
    long_length = len(line) * x
    short_length = len(line)
    found_i_index = -1
    found_k_index = -1

    result = ""
    for index in range(0, min(short_length * 100, long_length - 2)):
        result = multiply(result, get_long_digit(line, index))
        if result == "i":
            found_i_index = index
            break

    result = ""
    for index in range(long_length - 1, long_length - 1 - min(short_length * 100, long_length - 2), -1):
        result = multiply(get_long_digit(line, index), result)
        if result == "k":
            found_k_index = index
            break

    if found_i_index > -1 and found_k_index > -1 and found_k_index > found_i_index + 1:
        result = multiply_long_range(line, found_i_index + 1, found_k_index - 1)
        if result == "j":
            succeed = True
        else:
            succeed = False
    else:
        succeed = False

    print "Case #" + str(i + 1) + ": " + ("YES" if succeed else "NO")





