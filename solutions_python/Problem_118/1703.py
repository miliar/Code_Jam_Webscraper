import sys
import numpy as np

def is_palindrome(num):
    num_str = str(num)
    middle = len(num_str) / 2
    compensation = len(num_str) % 2
    return num_str[:middle] == num_str[middle + compensation:][::-1]

def is_fair_and_square(sqred_num, num):
    casted = int(sqred_num)
    return 1 if ((casted == sqred_num) and \
                     is_palindrome(num) and \
                     is_palindrome(casted)) else 0

def count_palindromes(bound):
    nums = np.arange(*bound)
    sqred_nums = np.sqrt(nums)
    vfairsquare = np.vectorize(is_fair_and_square)
    print len(np.nonzero(vfairsquare(sqred_nums, nums))[0])

if __name__ == "__main__":
    bounds = []
    with open(sys.argv[1], "r") as f:
        testcases = int(f.readline().strip())
        for case in xrange(testcases):
            bound = f.readline().strip().split(" ")
            start = int(bound[0])
            end = int(bound[1])+1
            bounds.append((start, end))

    case = 0
    for bound in bounds:
        case += 1
        print "Case #%d:" % (case,),
        count_palindromes(bound)
