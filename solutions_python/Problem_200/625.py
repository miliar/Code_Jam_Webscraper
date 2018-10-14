import fileinput


# Solve problem


def digit_list_from_number(number):
    return [int(digit) for digit in list(str(number))]


def number_from_digit_list(digit_list):
    return int("".join([str(digit) for digit in digit_list]))


def is_number_tidy(number):
    digit_list = digit_list_from_number(number)
    last_digit = 0
    for index, digit in enumerate(digit_list):
        if digit < last_digit:
            return False, index
        last_digit = digit

    return True, -1


def guess_prev_tidy_number(number, first_wrong_index):
    digit_list = digit_list_from_number(number)
    for i in range(first_wrong_index, len(digit_list)):
        digit_list[i] = 0
    number = number_from_digit_list(digit_list)
    return number - 1


def solve_problem(number):
    while number > 0:
        is_tidy, first_wrong_index = is_number_tidy(number)
        if is_tidy:
            return number
        number = guess_prev_tidy_number(number, first_wrong_index)


# Utils


def parse_problem(case):
    return int(case)


def solve_case(case, case_number):
    number = parse_problem(case)
    solution = solve_problem(number)
    print("Case #" + str(case_number) + ": " + str(solution))


# Main script

def main():
    for index, line in enumerate(fileinput.input()):
        if index is 0:
            continue

        line = line.strip()
        solve_case(line, index)

if __name__ == "__main__":
    main()
