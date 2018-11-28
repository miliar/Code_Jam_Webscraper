#!/usr/bin/env python

import argparse

def main():
  args = parseArgs()
  nCases = int(args.input.readline().strip('\n'))
  case = 0
  for line in args.input:
    case += 1
    smax = int(line.strip().split(' ')[0])
    audience = line.strip().split(' ')[1]
    nPeople = int(audience[0])
    nFriends = 0
    for s in range(1, smax+1):
      if (nPeople < s):
        nFriends += s - nPeople
        nPeople += s - nPeople
      nPeople += int(audience[s])
    print "Case #{}: {}".format(case, nFriends)
      
def parseArgs():
  parser = argparse.ArgumentParser()
  parser.add_argument('input', type=argparse.FileType('r'))
  return parser.parse_args()

main()