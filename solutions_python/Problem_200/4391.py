import sys

file_name = "B-small-attempt0"

sys.stdin = open(file_name + ".in")
sys.stdout = open(file_name + ".out", "w")

number_of_test_cases = int(input())


def check_tidy(number):
    list_number = list(str(number))
    for num in range(0, len(list_number)-1):
        if int(list_number[num]) > int(list_number[num+1]):
            return False
        else:
            continue
    return True

for testCase in range(1, number_of_test_cases + 1):
    case = int(input())
    number_of_tidy_number = 1
    for x in range(1, case + 1):
        if check_tidy(x):
            number_of_tidy_number = x
    print("Case #" + str(testCase) + ": " + ("%d" % number_of_tidy_number))
