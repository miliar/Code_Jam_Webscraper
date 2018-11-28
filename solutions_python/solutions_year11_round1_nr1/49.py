#!/usr/bin/python

ri = raw_input

T = int(ri())

def possible(n,pd,pg):
  if not (0 <= pg <= 100): return False
  if not (0 <= pd <= 100): return False
  if pd % 25 == 0: mind = 1
  elif pd % 5 == 0: mind = 5
  else: mind = 25
  if pd % 4 == 0: mind *= 1
  elif pd % 2 == 0: mind *= 2
  else: mind *= 4
  if n < mind: return False
  if pg in (0,100):
    return pg == pd
  return True

for t in xrange(T):
  n,pd,pg = map(int,ri().split())
  print "Case #%d:"%(t+1), "Possible" if possible(n,pd,pg) else "Broken"

