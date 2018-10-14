from __future__ import division

import sys, os

def do_case(ans_1, arrange_1, ans_2, arrange_2):
  pos = set(range(1,17))
  print ans_1
  print arrange_1
  print ans_2
  print arrange_2
  
  pos.intersection_update(arrange_1[ans_1 - 1])
  print pos
  pos.intersection_update(arrange_2[ans_2 - 1])
  print pos
  
  pos = list(pos)
  if len(pos) == 1:
    return pos[0]
  elif len(pos) == 0:
    return "Volunteer cheated!"
  elif len(pos) > 1:
    return "Bad magician!"
  return "fuck"
  


f = open(sys.argv[1], 'r')
out = open(sys.argv[2], 'w')

num_cases = int(f.readline())
for i in range(1,num_cases+1):
	ans_1 = int(f.readline())
	arrange_1 = []
	for j in range(4):
	  arrange_1.append(list(map(int, f.readline().split())))
	ans_2 = int(f.readline())
	arrange_2 = []
	for j in range(4):
	  arrange_2.append(list(map(int, f.readline().split())))
	  
	res = do_case(ans_1, arrange_1, ans_2, arrange_2)
	print "Case #%d:" % (i), res
	out.write("Case #%d: %s\n" % (i, res))

	
	