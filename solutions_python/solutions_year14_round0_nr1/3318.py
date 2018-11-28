#!/usr/bin/env python3

cases = int(input())

for case in range(1, cases+1):
  row1 = int(input())
  data1 = []
  for i in range(0, 4):
    data1.append(input().split(' '))

  row2 = int(input())
  data2 = []
  for i in range(0, 4):
    data2.append(input().split(' '))

  d1 = set(data1[row1-1])
  d2 = set(data2[row2-1])

  d = d1.intersection(d2)
  if len(d) == 0:
    out = "Volunteer cheated!"
  elif len(d) == 1:
    out = next(iter(d))
  else:
    out = "Bad magician!"

  print("Case #%d: %s" % (case, out))
