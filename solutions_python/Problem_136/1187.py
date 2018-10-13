#!/usr/bin/env python
#
# Copyright (c) 2013 NetApp, Inc.
# All rights reserved.
#
"""
"""

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
        input_values = [float(n) for n in data[i].split()]
        C = input_values[0]
        F = input_values[1]
        X = input_values[2]
        current_rate = 2.0
        num_cookies = 0.0
        total_time = 0.0
        done = False
        while not done:
            time_if_current_rate = (X/current_rate)
            time_if_next_rate = (C/current_rate) + (X/(current_rate+F))
            if time_if_current_rate > time_if_next_rate:
                total_time = total_time + (C/current_rate)
                current_rate = current_rate + F
            else:
                total_time = total_time + (X/current_rate) 
                done = True
        logger.info("Case #{0}: {1:.7f}".format(j+1,total_time))


if __name__ == "__main__":
    main()
