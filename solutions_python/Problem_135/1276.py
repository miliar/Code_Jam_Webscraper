#!/usr/bin/env python


def readTrial():
  selectedRow = int(raw_input())
  for r in range(1,5):
      row = raw_input()
      if r == selectedRow:
          ret = row.split()

  return ret

def results(common):
    l = len(common)
    if l > 1:
        return "Bad magician!"
    if l < 1:
        return "Volunteer cheated!"

    return "{}".format(common.pop())

      

tests = int(raw_input())

for t in range(1, tests+1):
    row1 = readTrial()
    row2 = readTrial()
    common = set(row1).intersection(set(row2))
    print "Case #{}: {}".format(t, results(common))

        
    

