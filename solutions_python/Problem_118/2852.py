#!/usr/bin/python
import math
filePrefix = 'C-small-attempt1'
fin = open(filePrefix + '.in', 'r')
fout = open(filePrefix + '.out', 'w')
T = int(fin.readline())


for i in range(T):
  low,high = tuple(fin.readline().strip().split())
  low = int(low)
  high = int(high)
  count = 0
  cursor = low
  while cursor <= high:
    if str(cursor) == str(cursor)[::-1]:
      cursor_root = math.sqrt(cursor)
      if cursor_root % 1 == 0:
          cursor_root = int(cursor_root)
          if str(cursor_root) == str(cursor_root)[::-1]:
            print "found %s with root %s" % (str(cursor), str(cursor_root))
            count+= 1
    cursor += 1
  
  fout.write("Case #%d: %s\n" % ((i+1), count))
#print(sorted(list(code_dict.values())))
