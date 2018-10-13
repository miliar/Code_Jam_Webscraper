import fileinput

no_of_tests = None
case_number = 1


def is_tidy(number_to_test):
    digits_in_list = [int(ele) for ele in list(str(number_to_test))]
    return all(digits_in_list[i] <= digits_in_list[i + 1] for i in range(0, len(digits_in_list) - 1))


def make_last_segment_tidy(number_to_change):
    digits_in_list = [int(ele) for ele in list(str(number_to_change))]
    anomaly_detected = False

    for i in range(0, len(digits_in_list)):

        if anomaly_detected:
            digits_in_list[i] = 9
            continue

        if digits_in_list[i] <= digits_in_list[i + 1]:
            continue

        anomaly_detected = True
        digits_in_list[i] -= 1

    return int("".join([str(ele) for ele in digits_in_list]))

for line in fileinput.input():

    if len(line) < 1:
        continue

    if no_of_tests is None:
        no_of_tests = int(line)
        continue

    number_counted = int(line)
    number_to_check = number_counted

    while not is_tidy(number_to_check):
        number_to_check = make_last_segment_tidy(number_to_check)

    print('Case #' + str(case_number) + ': ' + str(number_to_check))
    case_number += 1