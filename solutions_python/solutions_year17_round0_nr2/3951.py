import sys
from common.cases import write_cases_to_file

input = (line.strip() for line in sys.stdin if line.strip())
next(input)
# input = [sys.argv[1]]

def non_decreasing(number: str):
    digits = [int(digit) for digit in number]
    diff = (digits[i + 1] - digits[i] for i in range(0, len(digits) - 1))
    return all(digit >= 0 for digit in diff)


def find_previous_non_decreasing(number: str):
    digits = [int(digit) for digit in number]
    number = ''
    for i in range(len(digits) - 1):
        if digits[i + 1] - digits[i] < 0:
            return ''.join(map(str, digits[:i])) + str(digits[i] - 1) + '9' * len(list(map(str, digits[i + 1:])))


cases = []
for number in input:
    if non_decreasing(number):
        cases.append(number.strip('0'))
    else:
        while not non_decreasing(number):
            number = find_previous_non_decreasing(number)
        cases.append(number.strip('0'))

write_cases_to_file(cases, 'tidyoutput.txt')
