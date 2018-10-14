#!/usr/bin/env python

file = open('/home/ryan/Desktop/A-small-attempt1.in')
num_test_cases = file.readline()
lines = file.readlines()

t = 1
def toggle_snappers(it, powered, snappers):
  for i in range(len(powered)):
    j = len(powered)-i-1
    all_on = True
    for r in range(j):
      all_on = all_on and snappers[r]
    if all_on:
      snappers[j] = not snappers[j]
      if j+1 < len(powered):
        powered[j+1] = snappers[j]

for line in lines:
  n = int(line.split(' ')[0])
  k = int(line.split(' ')[1])

  powered = [False]*n
  powered[0] = True
  snappers = [False]*n
  for i in range(k):
    toggle_snappers(i, powered, snappers)

  all_snappered = True
  for snapper in snappers:
    all_snappered = all_snappered and snapper
  if all_snappered:
    print "Case #%s: %s" % (t,'ON')
  else:
    print "Case #%s: %s" % (t,'OFF')
  t+=1
  
  

