__author__ = 'hamekhan'


import math

def checkPalindrome(number):
    n = number
    reverse_num = 0
    while n > 0:
        last_digit = n % 10
        reverse_num = reverse_num * 10 + last_digit
        n = n / 10
    if number == reverse_num:
        return True
    else:
        return False

def startCase(start_num, end_num):
    start_num_sqrt = int(math.sqrt(start_num))-1
    end_num_sqrt = int(math.sqrt(end_num)) + 1
    palindrome_counts = 0
    for x in xrange(start_num_sqrt, end_num_sqrt):
        x_sqr = x**2
        if x_sqr >= start_num and x_sqr <= end_num:
            if checkPalindrome(x) and checkPalindrome(x**2):
                palindrome_counts += 1

    return palindrome_counts


def main():
    import sys, re
    pat = re.compile('([0-9]+)[^0-9]+([0-9]+)')
    number_of_cases = int(sys.stdin.readline().strip())
    case_num = 1
    while case_num <= number_of_cases:
        line = sys.stdin.readline()
        match = pat.match(line)
        start_num = int(match.group(1))
        end_num = int(match.group(2))
        palindrome_counts = startCase(start_num, end_num)
        print "Case #%d: %d" % (case_num, palindrome_counts)
        case_num += 1

if __name__ == "__main__":
    main()
