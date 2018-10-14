import sys
import numpy
import fileinput


def isPalindrome(numStr):
    return numStr == numStr[::-1]


# def isqrt(x):
#     if x < 0:
#         raise ValueError('square root not defined for negative numbers')
#     n = int(x)
#     if n == 0:
#         return 0
#     a, b = divmod(n.bit_length(), 2)
#     x = 2**(a+b)
#     while True:
#         y = (x + n//x)//2
#         if y >= x:
#             return x
#         x = y


def getCases(filename):

    with fileinput.input(files=filename) as f:
        # Don't need the first line (number of games)
        f.readline()
        cases = []

        line = f.readline()
        while line:
            cases.append(dict(zip(['min', 'max'], line.split())))
            line = f.readline()

        return cases


def testCase(case):
    palindromes = (num for num in range(int(case['min']), int(case['max']) + 1) if isPalindrome(str(num)))
    fair_and_square = (num for num in numpy.sqrt(list(palindromes)) if num.is_integer() and isPalindrome(str(int(num))))

    return sum(1 for x in fair_and_square)


def testCases(cases):
    result = ''
    i = 1

    for case in cases:
        result += "Case #{}: {}\n".format(i, testCase(case))
        i += 1

    return result


if __name__ == "__main__":
    filename = sys.argv[1]
    cases = getCases(filename)

    output_file = open(filename.replace('in', 'out'), 'w')
    output_file.write(testCases(cases))
    output_file.close()

    # print(timeit.timeit('isPalindrome("1234567890123456789008876543210987654322")', setup="from __main__ import isPalindrome", number=10000))
    # print(timeit.timeit('isqrt(1234567890123456789008876543210987654322)', setup="from __main__ import isqrt", number=10000))
    # print(timeit.timeit('math.sqrt(1234567890123456789008876543210987654322)', setup="import math", number=10000))
    # print(timeit.timeit('numpy.sqrt([1234567890123456789008876543210987654322])', setup="import numpy", number=10000))

    # print(math.sqrt(1234567890123456789008876543210987654322))
    # print(isqrt(1234567890123456789008876543210987654322))
    # print(numpy.sqrt([1234567890123456789008876543210987654322]))
