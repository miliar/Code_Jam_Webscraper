#!/usr/bin/python

f = open('pbots','r')
nlines = 0
num = 0
sec = 0
cur_pos_o = 1
cur_pos_b = 1
status_o = 0
status_b = 0

cmds_o = []
cmds_b = []

MOVE = 1
PUSH = 2
STAY = 3

for line in f.readlines():
  if(nlines == 0):
    num = int(line)
    nlines += 1
    continue
  
  nlines += 1

  parts = line.split(' ')
  numparts = int(parts[0])

  k = 0;

  for j in range(1, len(parts), 2):
    if parts[j] == "O":
      cmds_o.append((k,int(parts[j+1].rstrip())))
    elif parts[j] == "B":
      cmds_b.append((k,int(parts[j+1].rstrip())))
    k += 1

  cur_cmd = 0
  num_cmds = len(cmds_o) + len(cmds_b)

  while (len(cmds_o) + len(cmds_b)) > 0:  
  
    if(len(cmds_o) > 0):
      cur_o = cmds_o[0]
    if(len(cmds_b) > 0):
      cur_b = cmds_b[0]
    
    (num_o, pos_o) = cur_o
    (num_b, pos_b) = cur_b

    if len(cmds_o) > 0:
      if(cur_pos_o != pos_o):
        if(cur_pos_o < pos_o):
          cur_pos_o += 1
        else:
          cur_pos_o -= 1
        status_o = MOVE
      elif status_b != PUSH and num_o == cur_cmd:
        status_o = PUSH
        cmds_o.pop(0)
        cur_cmd += 1
      else:
        status_o = STAY

    if len(cmds_b) > 0: 
      if cur_pos_b != pos_b:
        if(cur_pos_b < pos_b):
          cur_pos_b += 1
        else:
          cur_pos_b -= 1
        status_b = MOVE
      elif status_o != PUSH and num_b == cur_cmd:
        status_b = PUSH
        cmds_b.pop(0)
        cur_cmd += 1
      else:
        status_b = STAY
   
    if status_o == PUSH:
      status_o = 0
    if status_b == PUSH:
      status_b = 0

    sec += 1

    #print "Time: %d" % sec 
    #print "Pos orange: %s" % cur_pos_o, "Pos blue: %s" % cur_pos_b

  print "Case #%d: %d" % (nlines-1, sec)
  cmds_o = []
  cmds_b = []
  sec = 0
  cur_pos_o = 1
  cur_pos_b = 1

f.close()
