#!/usr/bin/python

import sys
from collections import OrderedDict

f = open(sys.argv[1],'r')
t = int(f.readline())
def remove_dup(string):
  nd = ""
  for char in string:
    if len(nd) == 0 or (nd[len(nd)-1]!=char):
      nd += char
  return nd
for case in xrange(t):
  n = int(f.readline())
  no_dup = None
  edits = 0
  strings = []
  for i in xrange(n):
    string = f.readline().strip()
    string_nd = remove_dup(string)
    if no_dup == None:
      no_dup = string_nd
    elif no_dup != string_nd:
      edits = "Fegla Won"
      break
    nd_index = 0
    string_count = [0]*len(no_dup)
    for char in string:
      if(char == no_dup[nd_index]):
        string_count[nd_index] += 1
      else:
        string_count[nd_index+1] += 1
        nd_index += 1
    strings.append(string_count)
  if edits==0:
    med = [0]*len(no_dup)
    med_index = int(len(strings)/2)
    for i in xrange(len(no_dup)):
      med[i] = sorted(strings, key=lambda l:l[i])[med_index][i]
    for i in xrange(len(strings)):
      for j in xrange(len(no_dup)):
        edits += abs(strings[i][j]-med[j])
  print "Case #" + str(case+1) + ":", edits
