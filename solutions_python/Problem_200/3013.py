import re

def read_input_file():
    input_file = open("./B-large.in")
    line_text = input_file.readline()
    match_object = re.match("^(\d+)$", line_text)
    if match_object is not None:
        match_text = match_object.group(0)
        number_of_test_cases = int(match_text)
        print("Number of test cases:", number_of_test_cases)

    last_number_counted_list = []

    for x in range(number_of_test_cases):
        line_text = input_file.readline()
        match_object = re.match("^(\d+)$", line_text)
        if match_object is not None:
            last_number_counted_text = match_object.group(1)
            last_number_counted = int(last_number_counted_text)

        print("Last number counted:", last_number_counted)

        last_number_counted_list.append(last_number_counted)

    input_file.close()

    return number_of_test_cases, last_number_counted_list

def output_results_to_file(last_tidy_number_list):
    output_file = open("output_large.txt","w")
    for x in range(len(last_tidy_number_list)):
        write_text = ""
        if last_tidy_number_list[x]:
            write_text = "Case #"+str(x+1)+": "+str(last_tidy_number_list[x])+"\n"
        output_file.write(write_text)

    output_file.close()

def find_last_tidy_number(last_number_counted):
    is_number_tidy = False
    current_number = last_number_counted

    current_number_is_tidy = False
    iterations = 0
    while current_number_is_tidy is False and iterations < 10000:
        iterations += 1
        current_number_text = str(current_number)
        number_of_digits = len(current_number_text)

        current_tidy_digit_number = 0
        current_number_is_tidy = True
        current_digit = -1
        for x in range(number_of_digits):
            current_digit = x
            current_digit_number = int(current_number_text[x])
            if current_tidy_digit_number <= current_digit_number:
                current_tidy_digit_number = current_digit_number
            else:
                current_number_is_tidy = False
                break

        print("Current number", current_number," is tidy:", current_number_is_tidy)
        if current_number_is_tidy:
            break

        one_position_more_digit_value = int(current_number_text[current_digit-1])-1

        digits_counted = 0
        for x in range(current_digit, number_of_digits):
            digits_counted += 1

        insert_numbers = "9"
        if digits_counted > 1:
            for x in range(digits_counted-1):
                insert_numbers += "9"

        digits_inserted = len(insert_numbers)

        print("Current digit:", current_digit)
        current_number = int(current_number_text[:current_digit-1]+str(one_position_more_digit_value)+insert_numbers+current_number_text[current_digit+digits_inserted:])
        pass

    return current_number


def find_tidy_numbers_for_cases():
    number_of_test_cases, last_number_counted_list = read_input_file()

    last_tidy_number_list = []
    for x in range(number_of_test_cases):
        last_tidy_number = find_last_tidy_number(last_number_counted_list[x])
        last_tidy_number_list.append(last_tidy_number)

    output_results_to_file(last_tidy_number_list)

    return

if __name__ == "__main__":
    find_tidy_numbers_for_cases()