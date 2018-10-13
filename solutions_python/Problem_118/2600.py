import math
import sys


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        for nb_testcase in xrange(int(file.readline())):
            result = 0
            a, b = map(int, file.readline().split())
            a, b = int(math.ceil(math.sqrt(a))), int(math.sqrt(b)) + 1
            for i in range(a, b):
                if is_palindrome(i) and is_palindrome(i**2):
                    result += 1
            print "Case #%d: %d" % (nb_testcase + 1, result)
