def number_to_list(number):
    number_list = list()
    for numeral in str(number):
        if numeral == "\n":
            break
        number_list.append(int(numeral))
    return number_list


def list_to_number(number_list):
    number = 0
    multiplier = 1
    for numeral in number_list[::-1]:
        number += numeral * multiplier
        multiplier *= 10
    return number


def is_tidy(number_list):
    last_number = 1
    for number in number_list:
        if number < last_number:
            return False
        else:
            last_number = number
    return True


def print_case(case_number, number):
    print("Case #" + str(case_number) + ": " + str(number))


input_file = open("tests/B-large.in", "r")
number_of_cases = int(input_file.readline())
for case_number in range(1, number_of_cases + 1):
    number = int(input_file.readline())
    number_list = number_to_list(number)

    if not is_tidy(number_list):
        reverse_index = len(number_list) - 1
        multiplier = 1
        while not is_tidy(number_list):
            # Start subtracting so that the numerals at the end of the number
            # become '9'
            number = number - (number_list[reverse_index] + 1) * multiplier
            number_list = number_to_list(number)
            reverse_index -= 1
            multiplier *= 10
    print_case(case_number, number)
