#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sreyantha Chary
#
# Created:     13/04/2013
# Copyright:   (c) Sreyantha Chary 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import sqrt

def palindrome(i):
    string = str(i)
    rev = ''
    for letter in string:
        rev = letter + rev
    if string == rev:
        return True
    return False

answers = {}

def get_answer(lower_limit, upper_limit):
    count = 0
    for number in range(lower_limit, upper_limit+1):
        if answers.has_key(number):
            if answers[number]:
                count += 1
        else:
            if palindrome(number):
                if palindrome(pow(number, 2)):
                    count += 1
                    answers[number] = True
                else:
                    answers[number] = False
            else:
                answers[number] = False
    return count


test_cases = int(raw_input())
for i in range(test_cases):
    count = 0
    line = raw_input()
    [A, B] = line.split(' ')
    sqrA = sqrt(int(A))
    upper_limit = int(sqrt(int(B)))
    if sqrA == int(sqrA):
        lower_limit = int(sqrA)
    else:
        lower_limit = int(sqrA) + 1
    print "Case #%s: %s" % (str(i+1), str(get_answer(lower_limit, upper_limit)))
