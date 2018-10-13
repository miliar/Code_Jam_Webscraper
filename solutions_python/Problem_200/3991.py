import sys

input_file_path = sys.argv[1]


def find_last_tidy(number):
    while (number >= 0):
        # print("working on " + str(number))
        number_list = [int(d) for d in str(number)]
        if sorted(number_list) == number_list:
            return number
        number -= 1


with open(input_file_path) as input_file:
    test_case_count = int(input_file.readline())

    for test_case in range(test_case_count):
        number = int(input_file.readline())

        tidy_number = find_last_tidy(number)
        print("Case #" + str(test_case + 1) + ": " + str(tidy_number))
