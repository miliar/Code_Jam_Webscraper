import time
from sys import *
import copy 
import math    
import os
import collections
import itertools
import heapq
import sets
import random
import unittest

cases = int(raw_input())

def isPalindrone(number):
    i=0
    num =str(number)
    while i<len(str(num)):
        if num[0+i]!=num[-1-i]:
            return False
        i+=1
    return True


def solve(x, y):
    start= math.ceil(math.sqrt(x))
    end = math.floor(math.sqrt(y))
    counter = int(start)
    fair=0
    
    while counter<=end:
        if isPalindrone(counter):
            if isPalindrone(counter*counter):
                fair+=1               
        counter+=1
        
    return fair
    
for case in xrange(1, cases + 1):
    x, y = raw_input().split()
    x = int(x)
    y = int(y)    
    print "Case #%s: %s" % (case, solve(x, y))
