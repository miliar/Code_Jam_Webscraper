#!/usr/bin/env python
import sys

def readline(): return sys.stdin.readline().strip()
def readrow(): return readline().split(' ')

T = int(readline())
for t in range(T):
  row = readrow()
  c = int(row[0])
  del row[0]
  insts = []
  for b in range(c):
    insts.append((0 if row[b*2] == "B" else 1, int(row[b*2+1])))

  turn = 0
  currentInst = 0
  targetInst = [None, None]
  position = [1, 1]
  while currentInst < len(insts):
    turn += 1
    proceed = False
    for robot in range(2):
      if targetInst[robot] is None:
        for i in range(currentInst, len(insts)):
          inst = insts[i]
          if inst[0] == robot:
            targetInst[robot] = i
            break
      if targetInst[robot] is not None:
        inst = insts[targetInst[robot]]
        if inst[1] < position[robot]:
          position[robot] -= 1
        elif inst[1] > position[robot]:
          position[robot] += 1
        elif targetInst[robot] == currentInst:
          proceed = True
          targetInst[robot] = None
    if proceed: currentInst += 1
  print "Case #" + str(t+1) + ": " + str(turn)

