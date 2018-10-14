#! /usr/bin/env python3

import os
import os.path
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='tidy')
parser.add_argument("filename", help='Filename')

args = parser.parse_args()

class PancakeException(Exception):
    pass

def flip(s, index, size):
    if index + size > len(s):
        raise PancakeException
    for i in range(index, index+size):
        s[i] = '-' if s[i] == '+' else '+'
    
def run(s, size):
    s = list(s)
    num_flips = 0
    current = 0
    
    while True:
        while (s[current] == '+'):
            current += 1
            if current == len(s):
                return num_flips

        if current + size > len(s):
            raise PancakeException

        for i in range(current, current+size):
            if s[i] == '+':
                flip(s, i, size)
                num_flips += 1
                #print("num_flips={:3} {}".format(num_flips, "".join(s)))

        flip(s, current, size)
        num_flips += 1
        current += size
        if current == len(s):
            return num_flips
        print("num_flips={:3} {}".format(num_flips, "".join(s)))
                
outputfile = os.path.splitext(args.filename)[0] + ".out"

with open(args.filename, 'r') as f:
  with open(outputfile, 'w+') as fout:
    num_tests = int(f.readline().strip())
    for testcase in range(1,num_tests+1):
      s, size = f.readline().strip().split(' ')
      size = int(size)
      print("Case #{}: s={} k={}".format(testcase, s, size))

      try:
          result = run(s, size)
          print("{} flips".format(s, result))
          fout.write("Case #{}: {}\n".format(testcase, result))
      except PancakeException:
          print("IMPOSSIBLE".format(s))
          fout.write("Case #{}: IMPOSSIBLE\n".format(testcase))

