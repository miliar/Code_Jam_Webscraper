import sys, re

def find_next(s, f, steps):
  for i in range(f,len(steps)): 
    if steps[i][0]==s: 
      return i
  return -1

N = sys.stdin.readline()

for case in range(0,int(N)):
  seq = sys.stdin.readline().split()
  M = int(seq[0])
  seq = seq[1:len(seq)]
  steps = []
  for i in range(0,len(seq)-1,2):
    steps.append([seq[i], int(seq[i+1])])      
  res = 0

  where_O = 1
  where_B = 1
  can_jump_O = 0  
  can_jump_B = 0

  act_jump = 0
  for act in steps:
    if act[0]=="O":
      act_jump = max((abs(act[1]-where_O)-can_jump_O)+1, 1)
      can_jump_B += act_jump      
      can_jump_O = 0
      where_O = act[1]
    else: 
      act_jump = max((abs(act[1]-where_B)-can_jump_B)+1, 1)
#      print "jump:", can_jump_B, (abs(act[1]-where_B)-can_jump_B)+1
      can_jump_O += act_jump      
      can_jump_B = 0
      where_B = act[1]
    res+=act_jump
#    print act_jump

  print "Case #%d: %d" % (case+1,res)

