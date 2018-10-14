#!/usr/bin/python
import sys
import unittest
import math
Debug=False
from sys import stdin
#sys.setrecursionlimit(100000000)

def d(Str):
    if Debug: print Str

def run(data):
    if is_tidy(data):
        return data
    numl = to_numlist(data)
    #begin with with a flat numberg
    begin = flat_num(numl)
    newnum = to_int(begin) -1
    d("run with new num: %d from %d" % (newnum, data))
    return run(newnum)

def flat_num(numl):
    pos = get_max_pos(numl)
    for i in range(pos+1,len(numl)):
        numl[i] = 0
    return numl

def get_max_pos(numl):
    for i in range(0, len(numl)):
        if numl[i] == 0:
            return i
        if i >= 1 and numl[i] < numl[i-1]:
            return i - 1
    return len(numl) - 1

def is_tidy(numl):
    if type(numl) == int:
        numl = to_numlist(numl)
    curr = -1
    for i in range(0,len(numl)):
        if numl[i] >= curr:
            curr = numl[i]
        else:
            return False
    return True

def to_int(numl):
    return int("".join(map(str,numl)))


def to_numlist(num):
    return map(int, str(num))

class TestMe(unittest.TestCase):
    def test_to_numlist(self):
        self.assertEqual([8],to_numlist(8))
        self.assertEqual([1,2,3],to_numlist(123))
        self.assertEqual([5,5,5],to_numlist(555))
        self.assertEqual([2,2,2,4,4,4,8,8],to_numlist(22244488))
    def test_is_tidy(self):
        self.assertTrue(is_tidy(8))
        self.assertTrue(is_tidy(123))
        self.assertTrue(is_tidy(555))
        self.assertTrue(is_tidy(2244488))
        self.assertTrue(is_tidy(99999999999999999))

    def test_get_max_pos(self):
        self.assertEqual(2,get_max_pos(to_numlist(123)))
        self.assertEqual(2,get_max_pos(to_numlist(1900)))
        self.assertEqual(3,get_max_pos(to_numlist(1990)))
        self.assertEqual(3,get_max_pos(to_numlist(1999)))
        self.assertEqual(2,get_max_pos(to_numlist(127556)))
        self.assertEqual(1,get_max_pos(to_numlist(107556)))
        self.assertEqual(2,get_max_pos(to_numlist(110556)))
        self.assertEqual(0,get_max_pos(to_numlist(949975349403908273)))

    def test_flat_num(self):
        self.assertEqual(to_numlist(1999),flat_num(to_numlist(1999)))
        self.assertEqual(to_numlist(1900),flat_num(to_numlist(1987)))
        self.assertEqual(to_numlist(1280),flat_num(to_numlist(1287)))
        self.assertEqual(to_numlist(777890000),flat_num(to_numlist(777898787)))

    def test_to_int(self):
        self.assertEqual(123,to_int([1,2,3]))
        self.assertEqual(1230,to_int([1,2,3,0]))
        self.assertEqual(99,to_int([9,9]))

    def test_example(self):
        self.assertEqual(129,run(132))
        self.assertEqual(999,run(1000))
        self.assertEqual(7,run(7))
        self.assertEqual(99999999999999999,run(111111111111111110))
        #self.assertEqual(949975349403908273,run(949975349403908273))

if __name__ == '__main__':
    loops = int(stdin.readline())
    for i in range(0,loops):
        Data = int(stdin.readline())
        print "Case #%d: %s" % (i+1, str(run(Data)))
