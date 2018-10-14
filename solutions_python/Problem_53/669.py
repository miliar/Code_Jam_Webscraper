#!/usr/bin/python

from sys import stdin

def snapper_case(N, K):
  return (K + 1 - 2 ** N) % 2 ** N == 0

def sn2str(truth):
  if truth:
    return 'ON'
  else:
    return 'OFF'

# Read in all of the test cases.
num_cases = int(stdin.readline())

for n in range(0, num_cases):
  N, K = map(int, stdin.readline().split())
  print 'Case #' + str(n + 1) + ': ' + sn2str(snapper_case(N, K))
