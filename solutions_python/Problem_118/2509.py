# coding: utf-8
from IPython.nbformat import current
import math
from numpy.distutils.system_info import _numpy_info
from twisted.internet.test._posixifaces import in6_addr

__author__ = 'edubecks'

#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on April 12, 2013
@author: edubecks
"""

import os
import sys
import fileinput

DEBUG = True


def main():
    input_test = [line.strip() for line in fileinput.input()]

    num_tests = int(input_test[0])

    current_line = 1

    def is_palindrome(number):
        return str(number) == (str(number)[::-1])


    for test in xrange(num_tests):
        lim_min, lim_max = input_test[current_line].split()
        lim_min = int(lim_min)
        lim_max = int(lim_max)

        current_number = int(math.ceil(math.sqrt(lim_min)))

        counter = 0
        while True:
            square = current_number ** 2
            if square > lim_max:
                break
            if is_palindrome(current_number):
                if is_palindrome(square):
                    # if DEBUG: print current_number, square
                    counter += 1
            current_number += 1

        print 'Case #' + str(test + 1) + ': ' + str(counter)

        current_line += 1

    return


if __name__ == '__main__':
    main()
