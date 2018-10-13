#! /usr/bin/python

import sys

def solve(nb_assoc, assoc, nb_opposite, opposite, nb_elmt, elmt):
#  print elmt, assoc, opposite

  elmt_list = []
  opp_present = nb_opposite * [-1]

  for e in elmt:
#    print "*", elmt_list, opp_present
    elmt_list += e
    combined = False
    if len(elmt_list) >= 2:
      elmt_check = [ elmt_list[-2], elmt_list[-1] ]
      for a in assoc:
        if elmt_check == a[0]:
          elmt_list.pop()
          elmt_list.pop()
          elmt_list.append(a[1])
          combined = True
          for k in range(nb_opposite):
            if opp_present[k] > len(elmt_list) - 2:
              opp_present[k] = -1
          break

    if not combined:
      for k in range(nb_opposite):
        o = opposite[k]
        if opp_present[k] != -1 and elmt_list[-1] == o[1]:
          elmt_list = []
          opp_present = nb_opposite * [-1]
          break
        elif opp_present[k] == -1 and elmt_list[-1] == o[0]:
          opp_present[k] = len(elmt_list) - 1

  return repr(elmt_list).replace("'", "")
      
fd = open(sys.argv[1])

num_cases = int(fd.readline())

for i in range(0, num_cases):
  from collections import deque
  a = deque(fd.readline().split(" "))

  nb_assoc = int(a.popleft())
  assoc = []
  for j in range(nb_assoc):
    ass = a.popleft()
    assoc.append([[ass[0], ass[1]], ass[2]])
    assoc.append([[ass[1], ass[0]], ass[2]])

  nb_opposite = int(a.popleft())
  opposite = []
  for j in range(nb_opposite):
    opp = a.popleft()
    opposite.append([opp[0], opp[1]])
    opposite.append([opp[1], opp[0]])

  nb_elmt = int(a.popleft())
  elmt = list(a.popleft()[:-1])

  output = solve(2 * nb_assoc, assoc, 2 * nb_opposite, opposite, nb_elmt, elmt)
  print "Case #%d:" % (i+1), output

