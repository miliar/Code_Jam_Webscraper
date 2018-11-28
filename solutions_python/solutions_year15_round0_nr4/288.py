#!/usr/bin/env python
#
# Copyright (c) 2013 NetApp, Inc.
# All rights reserved.
#
"""
"""
# IMPORTANT
# Run as 
# python template.py < A-small-practice.in >& A-small-practice.out

from __future__ import print_function
import argparse
import getpass
import glob
import imp
import itertools
import logging
import pkg_resources
import pkgutil
import sys
import re
import ystockquote
import requests
import threading
from multiprocessing import Process
import time
import bisect


# This function will take a certain number, and generate the 'base' representation
# of it. And it will output that in the form of a array ..
# you have to provide how many 'bits' you want .. if there are excess, the leading
# ones will be zero.
def convert_number_to_bit_string(number, num_bits, base=2):
    string_bits = [0 for i in range(num_bits)]
    index = len(string_bits) - 1
    while index >= 0:
        string_bits[index] = number%base
        number = number / base
        index = index -1
    return string_bits

#USE THE function bisect.insort() whenever necessary
#If a is sorted in ascending order, e.g a = [5, 7, 10, 17]
# bisect.insort(a, 12) will insert 12 into the sorted array using binary search.
# bisect.insort(a, 12) will result in [5, 7, 10, 12, 17]

logger = logging.getLogger(__name__)

def main():
    streamformat = "%(message)s"
    logging.basicConfig(level=logging.INFO,
                        format=streamformat)
    data = sys.stdin.readlines()
    i = 0
    nums = [int(n) for n in data[i].split()]
    num_test_cases = nums[0]
    for j in range(num_test_cases):
        i = i + 1
        nums = [int(n) for n in data[i].split()]
        X = nums[0]
        R = nums[1]
        C= nums[2]
        temp_r = R
        if R > C:
            R = C
            C = temp_r 
        answer = None
        if X == 1:
            answer = "GABRIEL"
        elif X == 2:
            if (R*C)%2 == 0:
                answer = "GABRIEL"
            else:
                answer = "RICHARD"
        elif X == 3:
            if (R*C)%3 != 0:
                answer = "RICHARD"
            elif ((C == 3 and R == 1) or (C==4 and R == 2)):
                answer = "RICHARD"
            else:
                answer = "GABRIEL"
        elif X == 4:
            if (R*C)%4 != 0:
                answer = "RICHARD"
            elif ((C == 2 and R == 2) or (C==4 and R == 1) or (C==4 and R ==2)):
                answer = "RICHARD"
            else:
                answer = "GABRIEL"
        logger.info("Case #{0}: {1}".format(j+1, answer))

if __name__ == "__main__":
    main()
