from math import sqrt, trunc, ceil


def is_palindrome(num):
    num_list = list(str(num))
    if num_list == num_list[::-1]:
        return True
    return False


file_input = open('2.input')
file_output = open('2.output', 'w+')

number_tests = int(file_input.readline())

for test in xrange(1, number_tests + 1):

    start, end = map(int, file_input.readline().split())
    count = 0
    # get first sqrt
    current_sqrt = int(ceil(sqrt(start)))
    square = current_sqrt * current_sqrt
    while square <= end:
        if is_palindrome(current_sqrt) and is_palindrome(square):
            count += 1
        current_sqrt += 1
        square = current_sqrt * current_sqrt

    file_output.write("Case #{0}: {1}\n".format(test, count))
