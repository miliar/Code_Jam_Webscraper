# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import sys
from operator import mul
def find_next(todo, robo, start):
  for r, n in todo[start:]:
    if r==robo:
      return n
  return -1
f = open(sys.argv[1],"r")
T = int(f.readline())
for t in range(T):
  l = f.readline().split()
  C = int(l[0])
  combine_rules = l[1:C+1]
  D = int(l[C+1])
  opposed_rules = l[C+2:C+2+D]
  N = int(l[C+2+D])
#  print l, C, D, N
  invoked_elements = l[C+3+D]
#  print combine_rules
#  print opposed_rules 
#  print invoked_elements
  assert len(l) == C+4+D
  assert len(invoked_elements) == N
  assert len(combine_rules) == C
  assert len(opposed_rules) == D
  combine = {}
  for c in combine_rules:
    assert len(c) == 3
    combine[c[0]+c[1]] = c[2]
    combine[c[1]+c[0]] = c[2]
  opposed = {}
  for d in opposed_rules:
    assert len(d) == 2
    x, y = d[0],d[1]
    if opposed.has_key(x):
      opposed[x].append(y)
    else:
      opposed[x]=[y]
    if opposed.has_key(y):
      opposed[y].append(x)
    else:
      opposed[y]=[x]
#  print combine
#  print opposed
  element_list = ""
  element_dict = {}
  for e in invoked_elements:
    element_list += e
    if element_dict.has_key(e):
      element_dict[e] += 1
    else:
      element_dict[e] = 1
#    print "adding %c gives %s"%(e,element_list)
    if len(element_list)<2:
      continue
    if element_list[-2:] in combine:
#      print "combining %s to %c gives" %(element_list[-2:],
#	  combine[element_list[-2:]]),
      element_dict[element_list[-2]] -=1
      element_dict[element_list[-1]] -=1
      element_list = element_list[:-2]+combine[element_list[-2:]]
      if element_dict.has_key(element_list[-1]):
	element_dict[element_list[-1]] += 1
      else:
	element_dict[element_list[-1]] = 1
#      print element_list, element_dict
    elif element_list[-1] in opposed.keys():
      opp = False
      for x in opposed[element_list[-1]]:
	if x in element_dict.keys():
	  if element_dict[x] != 0:
#	    print "is opposed"
	    opp = True
	    break
      if opp:
#	print "cleanup"
	element_list = ""
	element_dict = {}
  print "Case #%d: [%s]"%(t+1, ", ".join(element_list))
