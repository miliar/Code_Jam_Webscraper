#!/usr/bin/env python
# encoding: utf-8

import sys
import os

table = {'a': 'y', ' ': ' ', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}


def translate(case):
  return "".join([table[c] for c in case])


def main(argv):
	testcases = sys.stdin.readline().strip()
	for testcase in range(int(testcases)):
	  case = sys.stdin.readline().strip()
	  plaintext = translate(case)
	  sys.stdout.write("Case #%d: %s\n" % (testcase + 1, plaintext))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))

