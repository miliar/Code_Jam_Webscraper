import bisect
import math
import pprint
import string
import sys

max_digits = 14

def enumerateAll(max_digits):
    return range(1, 10**max_digits)

def generatePalindromes():
    # Generate a list of palindromes up to 10^7
    palindromes = range(10)  # special single-digit cases

    # palindromes are ([1-9]*)[0-9]?\1
    max_pre = int(math.floor(max_digits / 2)) + 1
    for num_digits in range(1, max_pre):
        print num_digits, "num_total", len(palindromes)
        mult = 10**num_digits
        def combine2(a, b):
            return a * mult + int(str(b)[::-1])

        def combine3(a, b, c):
            return a * (mult * 10) + b * mult + int(str(c)[::-1])
        all_pre = enumerateAll(num_digits)
        palindromes.extend(map(combine2, all_pre, all_pre))
        for pre in all_pre:
            for middle in range(10):
                palindromes.append(combine3(pre, middle, pre))
#palindromes = generatePalindromes()

def largeRange(stop):
   i = 0
   while i < stop:
       yield i
       i += 1

def isPalindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]


def generateFairAndSquares():
    max_root = int(math.ceil(math.sqrt(10**max_digits)))
    fair_and_squares = []
    for i in largeRange(max_root):
        if isPalindrome(i) and isPalindrome(i * i):
            fair_and_squares.append(i * i)
        if len(str(i)) != len(str(i + 1)):
            print len(str(i)), 'digits', 'total squares:', len(fair_and_squares)
    print (i + 1) ** 2, "is at least", 10**max_digits, "and is ", max_digits + 1, "digits"
    return fair_and_squares

fair_and_squares = generateFairAndSquares()
print fair_and_squares

def numFairAndSquares(a, b):
    l_index = bisect.bisect_left(fair_and_squares, a)
    r_index = bisect.bisect_right(fair_and_squares, b)
    count = 0
    for i in xrange(l_index, r_index):
        count += 1
    return count

def main(in_fd, out_fd):
    n = int(in_fd.readline())
    for i in range(n):
        a, b = map(int, in_fd.readline().strip().split())
        n = numFairAndSquares(a, b)
        write_output(out_fd, i, n)

def write_output(out_fd, i, output):
    out_fd.write('Case #{0}: {1}\n'.format(i + 1, output))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Need file name"
        sys.exit(1)
    in_name = sys.argv[1]
    out_name = string.replace(in_name, ".in", ".out")
    with open(in_name) as in_fd:
        with open(out_name, 'w') as out_fd:
            main(in_fd, out_fd)
