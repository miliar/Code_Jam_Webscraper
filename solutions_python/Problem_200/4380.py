#!/usr/bin/python3
def is_tidy(number):
    if len(number) == 1:
        return number
    else:
        result = ''
        for i in range(1, len(number)):
            if number[i-1] <= number[i]:
                result += number[i-1] + is_tidy(number[i:])
            else:
                result += str(int(number[i-1]) - 1) + '9' * (len(number) - i)
            return result

with open('b.in') as data_set_file:
    number_of_test_cases = data_set_file.readline()
    results = []
    for index, test_case in enumerate(data_set_file.readlines()):
        test_case = test_case.replace('\n', '')
        while(not all(test_case[i] <= test_case[i+1] for i in range(len(test_case)-1))):
            test_case = is_tidy(test_case)
        print("Case #{}: {}".format(index+1, int(test_case)))
