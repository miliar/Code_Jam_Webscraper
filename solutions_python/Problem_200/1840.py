# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
# 4
# 132
# 1000
# 7
# 111111111111111110
import re

def _int2list(number):
    s = str(number)
    digits = []
    for c in s:
        digits.append(int(c))
    return digits



def _is_tidy(n):
    digits_unsorted = _int2list(n)
    digits_sorted = _int2list(n)
    digits_sorted.sort()
    #print("Seeing if %d is tidy   digits:%s" % (n, digits_unsorted))
    #print("Comparing %s with %s" % (digits_unsorted, digits_sorted))
    tidy = digits_sorted == digits_unsorted
    return tidy


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    digits = _int2list(n)
    #print("Case #{}: INPUT {} --> {}".format(i, n, digits))

    n_candidate = n
    while not _is_tidy(n_candidate):
        # find first place sequence increases
        found_untidiness = False
        j = 0
        while j+1 < len(digits) and not found_untidiness:
            if digits[j] > digits[j+1]:
                found_untidiness = True
            else:
                j += 1

        if found_untidiness:
            #print("Found untidiness, fixing")
            digits[j] = digits[j]-1
            for k in range(j+1, len(digits)):
                digits[k] = 9
        s = ''
        for c in digits:
            s = s + str(c)
        n_candidate = int(s)

    print("Case #{}: {}".format(i, n_candidate))