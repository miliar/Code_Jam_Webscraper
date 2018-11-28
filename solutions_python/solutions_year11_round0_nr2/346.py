#!/usr/bin/python

from collections import defaultdict

ri = raw_input
for t in xrange(int(ri())):
  test = ri().split()
  c = int(test[0])
  combine = {}
  for xyz in test[1:c+1]:
    combine[xyz[0],xyz[1]] = combine[xyz[1],xyz[0]] = xyz[2]
  d = int(test[c+1])
  oppose = defaultdict(list)
  for xy in test[c+2:c+2+d]:
    oppose[xy[0]].append(xy[1])
    oppose[xy[1]].append(xy[0])
  lst = []
  for elt in test[-1]:
    if lst and (elt,lst[-1]) in combine:
      lst[-1] = combine[elt,lst[-1]]
    elif elt in oppose:
      killed = False
      for opp in oppose[elt]:
        if opp in lst:
          lst = []
          killed = True
          break
      if not killed:
        lst.append(elt)
    else:
      lst.append(elt)
  print "Case #%d: [%s]" %(t+1,", ".join(lst))
    
