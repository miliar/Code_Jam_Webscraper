#!/usr/bin/env python

def solve(case_nr):
  [N, R, O, Y, G, B, V] = map(int, raw_input().split())
  
  l = [(R,'R'), (O,'O'), (Y,'Y'), (G,'G'), (B,'B'), (V,'V')]
  
  pos1=max(l)
  l.remove(pos1)
  pos2=max(l)
  l.remove(pos2)
  pos3=max(l)
  l.remove(pos3)
  
  answer = 'IMPOSSIBLE'
  
  if (pos2[0]+pos3[0]) >= pos1[0]:
    sections = [[pos1[1]] for i in xrange(pos1[0])]
    i = 0
    count = pos2[0]
    while count > 0:
      sections[i].append(pos2[1])
      i = (i + 1) % len(sections)
      count = count - 1
    count = pos3[0]
    while count > 0:
      sections[i].append(pos3[1])
      i = (i + 1) % len(sections)
      count = count - 1
    
    answer = "".join(["".join(section) for section in sections])
  
  print "Case #%d: %s" % (case_nr, answer)


T = int(raw_input())

for i in xrange(T):
  solve(i+1)
