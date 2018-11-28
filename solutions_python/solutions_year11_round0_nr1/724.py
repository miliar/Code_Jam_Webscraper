#!/usr/bin/env python2.6

import sys

def signum(i):
  if i<0: return -1
  elif i>0: return 1
  else: return i

def action(name):
  for act in SEQ:
    if act[0] == name:
      val = int(act[1:])-POS.get(name)
      index = SEQ.index(act)
      if index == 0 and val == 0:
        return 2 # PRESS
      else: return signum(val) # MOVE | WAIT
  return 0 # no more action, WAIT

T = 0
Ti = 0
POS = {'O':1,'B':1}
SEQ = []

for line in sys.stdin:
  if Ti == 0:
    T = int(line.strip())
    Ti = 1
    continue
  if SEQ: print 'ERROR#2 BRO'
  l = line.strip().split(' ')
  for i in range(1,len(l),2):
    SEQ.append(l[i]+str(l[i+1]))

  count = 0
  while(SEQ):
    OACT = action('O')
    BACT = action('B')
    if OACT == 2 and BACT == 2: print 'ERROR BRO'
    if OACT == 2:
      SEQ.remove(SEQ[0]) # O pressed button
      POS.update({'B': POS.get('B')+BACT})
    elif BACT == 2:
      SEQ.remove(SEQ[0]) # B pressed button
      POS.update({'O': POS.get('O')+OACT})
    else:
      POS.update({'O': POS.get('O')+OACT, 'B': POS.get('B')+BACT})

    count+=1

  print 'Case #%d: %d' % (Ti, count)

  POS.update({'O':1,'B':1})
  Ti+=1
  if Ti>T: break
