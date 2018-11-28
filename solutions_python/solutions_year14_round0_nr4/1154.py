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
        i = i+1
        nums = [int(n) for n in data[i].split()]
        N = nums[0]
        i = i+1
        Naomi = [float(n) for n in data[i].split()]
        i = i+1
        Ken = [float(n) for n in data[i].split()]
        SortNaomi = sorted(Naomi)
        SortKen = sorted(Ken)
        score = play_war(SortNaomi, SortKen, N)
        SortNaomi = sorted(Naomi)
        SortKen = sorted(Ken)
        #logger.info("Case #{0}: {1} {2} Naomi is {3} Ken is {4}".format(j+1, score, score, SortNaomi, SortKen))
        deceit_score = play_deceit_war(SortNaomi, SortKen, N)
        logger.info("Case #{0}: {1} {2}".format(j+1, deceit_score, score))

def play_war(Naomi, Ken, N):
    naomi_score = 0
    for i in range(N):
        naomi_value = Naomi[N-1-i]
        index_val = get_index_of_next_highest(Ken, len(Ken), naomi_value)
        if index_val == -1:
            Ken.pop(0)
            naomi_score = naomi_score + 1
        else:
            Ken.pop(index_val)
    return naomi_score

def play_deceit_war(Naomi, Ken, N):
    naomi_score = 0
    for i in range(N):
        if Naomi[len(Naomi)-1] < Ken[len(Ken)-1]:
            ken_index = get_index_of_next_highest(Ken, len(Ken), Naomi[len(Naomi)-1])
            ken_value = Ken[ken_index]
            Ken.pop(ken_index)
            index_val = get_index_of_next_lowest(Naomi, len(Naomi), ken_value)
            if index_val != -1:
                Naomi.pop(0)
            else:
                index_val = get_index_of_next_highest(Naomi,len(Naomi), ken_value)
                Naomi.pop(index_val)
                naomi_score = naomi_score + 1
        else:
            ken_value = Ken[0]
            naomi_index = get_index_of_next_highest(Naomi, len(Naomi), ken_value)
            Ken.pop(0)
            Naomi.pop(naomi_index)
            naomi_score = naomi_score + 1 
    return naomi_score

def get_index_of_next_highest(Array, N, value):
    for i in range(N):
        if (Array[i] > value):
            return i
    return -1
        
def get_index_of_next_lowest(Array, N, value):
    for i in range(N):
        if (Array[N-1-i] < value):
            return i
    return -1

if __name__ == "__main__":
    main()
