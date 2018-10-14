import code_jam


def get_trailing_tidy_number(number):
    last_digit = 0
    result = list()

    for i in number:
        if int(i) >= last_digit:
            result.append(i)
            last_digit = int(i)
        else:
            break
    return ''.join(result)


def get_max_tidy_number_lower_than(number):
    digits = len(number)
    trailing_tidy_number = get_trailing_tidy_number(number)
    trailing_digits = len(trailing_tidy_number)
    if number == trailing_tidy_number:
        return number
    else:
        return str(int(get_max_tidy_number_lower_than(str(int(trailing_tidy_number) - 1)) + (digits - trailing_digits)*'9'))


def get_output_data(input_data):
    output_data = list()
    for item in input_data:
        case_number = len(output_data) + 1
        item_output = get_max_tidy_number_lower_than(item)
        output_data.append("Case #{}: {}".format(case_number, item_output))
    return output_data

input_file = './tidy_numbers/TidyNumbers.Large.in'
output_file = './tidy_numbers/TidyNumbers.Large.out'

input_data = code_jam.read_input_data(input_file)
code_jam.write_output_data(output_file, get_output_data(input_data))


