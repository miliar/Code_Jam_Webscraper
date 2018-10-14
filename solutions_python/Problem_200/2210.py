""" Tidy numbers problem - find last number in range with ascending digits"""
from sys import stdin

def check_tidy(digit_string):
    if len(digit_string) < 2:
        return True, 0
    for i in range(len(digit_string)-1, 0, -1):
        if digit_string[i] < digit_string[i-1]:
            return False, i-1
    return True, 0

def solve_tidy_numbers(digit_string):
    tidy, untidy_point  = check_tidy(digit_string)
    if tidy:
        return digit_string
    while not tidy:
        # print("Digit String", digit_string)
        # print("Untidy point", untidy_point)
        if digit_string[untidy_point] == '0' or (untidy_point == 0 and digit_string[0] == '1'):
            return '9'*(len(digit_string)-1)
        else:

            string_begin = digit_string[: untidy_point]
            # print("String begin", string_begin)
            decrement_untidy = chr(ord(digit_string[untidy_point]) - 1)
            # print("Decrement", decrement_untidy)
            following = '9'*len(digit_string[untidy_point + 1:])
            # print("Following", following)
            digit_string = string_begin + decrement_untidy + following
        tidy, untidy_point = check_tidy(digit_string)
        if tidy:
            return digit_string

def main():
    test_cases  = int(stdin.readline())
    for i in range(1, test_cases + 1):
        digit_string = stdin.readline().strip()
        result = solve_tidy_numbers(digit_string)
        print("Case #%s: %s" % (str(i), result))

main()
