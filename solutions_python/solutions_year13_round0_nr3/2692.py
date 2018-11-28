import sys
import math

data = file(sys.argv[1]).read().strip().split("\n")

def print_result(result, num):
    print "Case #%d: %d" % (num, result)

def palindrome(str):
    if str == str[::-1]:
        return True
    return False

test_num = 1
for line in data[1:]:
    counter = 0
    lower, upper = line.split(" ")
    for i in range(int(lower), int(upper) + 1):
        if palindrome(str(i)) and int(math.sqrt(i))**2 == i and palindrome(str(int(math.sqrt(i)))):
            counter += 1
    print_result(counter, test_num)
    test_num += 1
