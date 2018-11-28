#!/usr/bin/python

import sys
import fileinput

def process(infile, case):

  line = infile.readline()
  split = line.split()
  N = int(split[0])
  M = int(split[1])

  root = {}

  #read the directory tree
  for i in range(0, N):
    dirEntry = infile.readline().strip()
    dirEntry = dirEntry.strip()
    directories = dirEntry.split('/')

    pathSoFar = root
    for dir in directories[1:]:
      if pathSoFar.has_key(dir):
        pathSoFar = pathSoFar[dir]
      else:
        pathSoFar[dir] = {}
        pathSoFar = pathSoFar[dir]
    

  #read the test cases
  numOps = 0

  for i in range(0, M):
    line = infile.readline()
    line = line.rstrip()
    split = line.split('/')
  
    #print "test line = ", line

    path = root
    #print "==="
    for subdir in split[1:]:
      #print "path so far = ", path
      #print "root so far = ", root
      #print "subdir = ", subdir
      if path.has_key(subdir):
        path = path[subdir]
      else:
        path[subdir] = {}
        path = path[subdir]
        numOps += 1 

    #print root

  print "Case #%d: %d" %(case, numOps)
  case = case + 1
  return case
# process


def main():

  infile = open(sys.argv[1], 'r')

  case = 1
  count = int(infile.readline())

  for i in range(0, count):
    case = process(infile, case)
#main


if __name__ == "__main__":
  main()
