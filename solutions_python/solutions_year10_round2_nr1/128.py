#!/usr/bin/python

import sys

def main(argc, argv):
  ifile = open(argv[1], 'r')

  case_num = int(ifile.readline()[:-1])

  for case in range(1, case_num+1):
    existing = set([])
    created = 0
    line = ifile.readline()
    existing_num, to_create_num = map(int, line.split())
    for i in range(0, existing_num):
      dir = ifile.readline()[:-1]
      existing.add(dir)

    for i in range(0, to_create_num):
      dir = ifile.readline()[:-1]
      if not(dir in existing):
        path = dir.split("/")[1:]
        dir = ""
        for j in range(0, len(path)):
          dir = dir + "/" + path[j] 
          if not(dir in existing):
            existing.add(dir)
            created += 1

    print "Case #" + str(case) + ": " + str(created)



if __name__ == "__main__":
  main(len(sys.argv), sys.argv)
