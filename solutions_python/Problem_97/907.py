#!/usr/bin/env python
# encoding: utf-8

import sys
import os


def main():
	testcases = sys.stdin.readline().strip()
	for testcase in range(int(testcases)):
	  case = sys.stdin.readline().strip()
	  a, b = case.split()
	  a, b = int(a), int(b) + 1
	  tested = []
	  recycled = 0
	  
	  for i in range(a, b):
	    candidate = str(i)
	    if len(set([c for c in candidate])) == 1:
	      continue
	    for j in range(1, len(candidate)):
	      new_num = int(candidate[-j:] + candidate[:-j])
	      if new_num > i and new_num >= a and new_num < b and not (i, new_num) in tested:
	        recycled += 1
	        tested.append((i, new_num))
	  sys.stdout.write("Case #%d: %d\n" % (testcase + 1, recycled))


if __name__ == '__main__':
	main()

