#!/usr/bin/python

import re
import sys
import math

input_file = sys.stdin


test_cases_num = int (input_file.readline ())


def is_palindrome (string):
    length = len (string)
    if (length % 2 == 0):
        for i in xrange (0, length / 2):
            if (string[i] != string[length - 1 - i]):
                return False
    else:
        for i in xrange (0, int (math.floor (length / 2))):
            if (string[i] != string[length - 1 - i]):
                return False

    return True



for case_num in xrange (1, test_cases_num + 1):
    line = input_file.readline ().split (' ')
    A = int (line[0])
    B = int (line[1])

    cache = [False for x in range (A, B + 1)]
    count = 0
    for i in reversed (xrange (A, B + 1)):
        if (cache[i - A]):
            continue
        #print str (i) + ' is a palindrome? ' + str (is_palindrome (str (i)))

        if (is_palindrome (str (i))):
            i_rooted = math.sqrt (i) 
            if (i_rooted - math.floor (i_rooted) != 0):
                continue
            #print '    ' + str (i_rooted) + ' is a palindrome? ' + str (is_palindrome (str (int (i_rooted))))
            if (is_palindrome (str (int (i_rooted)))):
                count += 1
            else:
                cache[i - A] = True


    print 'Case #' + str (case_num) + ': ' + str (count)


