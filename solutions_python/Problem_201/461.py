#! /usr/bin/env python3

import os
import os.path
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='tidy')
parser.add_argument("filename", help='Filename')

args = parser.parse_args()

outputfile = os.path.splitext(args.filename)[0] + ".out"

def place(num_stalls, num_persons):
    ranges = {num_stalls: 1}
    to_place = num_persons
    while True:
        #print("To place: {}".format(to_place))
        current = max(ranges.keys())
        num_available = ranges[current]
        del ranges[current]
        new_left = (current - 1) // 2
        new_right = current - new_left - 1
        if num_available >= to_place:
            print("{:4} {:4}: {:3} {:3}".format(num_stalls, num_persons, new_right, new_left))
            return new_right, new_left
        ranges[new_left] = ranges.get(new_left, 0) + num_available
        ranges[new_right] = ranges.get(new_right, 0) + num_available
        #pprint(ranges)
        to_place -= num_available


with open(args.filename, 'r') as f:
  with open(outputfile, 'w+') as fout:
    num_tests = int(f.readline().strip())
    for testcase in range(1,num_tests+1):
      num_stalls, num_persons = map(int, f.readline().strip().split(' '))
      print("Case #{}: {} stalls, {} people".format(testcase, num_stalls, num_persons))
      right, left = place(num_stalls, num_persons)
      print("Right = {:4}, left = {:4}".format(right, left))
      fout.write("Case #{}: {} {}\n".format(testcase, right, left))
