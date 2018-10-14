import os

cache = {}


def is_tidy(num):

    if num in cache:
        return cache[num]

    string_number = str(num)
    if len(string_number) == 1:
        cache[num] = True
        return True

    if not is_tidy(string_number[:-1]):
        cache[num] = False
        return False

    if int(string_number[-2]) > int(string_number[-1]):
        cache[num] = False
        return False
    else:
        cache[num] = True
        return True


def last_tidy_num(num):
    print num

    while num >= 1:
        if is_tidy(num):
            return num

        str_num = str(num)
        last_digit = str_num[0]
        digits = last_digit
        for index, current_digit in enumerate(str_num[1:]):
            if current_digit < last_digit:
                digits += "0" * (len(str_num) - (index + 1))
                break
            last_digit = current_digit
            digits += current_digit
        num = int(digits) - 1
    return num


def main():

    input_filename = os.path.splitext(os.path.basename(__file__))[0]+".in"
    input_file = open(input_filename, "r")

    output_filename = os.path.splitext(os.path.basename(__file__))[0]+".out"
    output_file = open(output_filename, "w")

    case_count = int(input_file.readline())

    for i in range(case_count):

        last_count_number = int(input_file.readline())
        last_tidy_number = last_tidy_num(last_count_number)

        output_line = "Case #%s: %s\n" % (i+1, last_tidy_number)
        output_file.write(output_line)


if __name__ == '__main__':
    main()
