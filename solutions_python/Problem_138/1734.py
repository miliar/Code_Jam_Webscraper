#!/usr/bin/python

import sys
import copy 

input_file = open(sys.argv[1], "r")
flag = 0 # toss 1rst line
step = 0
case1 = 0
for line in input_file:
  if flag == 1:
    token = line.split()
    if ( step == 0 ):
      step = 1
      blocks = int(token[0])
    elif ( step == 1 ):
      naomi = copy.deepcopy(token)
      d_naomi = copy.deepcopy(token)
      step = 2
    elif ( step == 2 ):
      ken = copy.deepcopy(token)
      d_ken = copy.deepcopy(token)
      step = 3
    # time to play    
    if ( step == 3 ):
      case1 = case1 + 1
      print ("Case #{0}:".format(case1)),
      step = 0
      win = 0
      d_win = 0
      #dirty war
      for x in range(0,blocks):
        chosen_naomi = min( d_naomi, key=float)
        max_ken = max(d_ken, key=float)
        min_ken = min(d_ken, key=float)
        min_naomi = min(d_naomi, key=float)
        d_naomi.remove(chosen_naomi)
        if ( max_ken < chosen_naomi):
          told_naomi = float(chosen_naomi)
        elif ( float(min_ken) < float(min_naomi) and float(max_ken) < 1.0 ):
          told_naomi = float(max_ken) + 0.00000001
        else:
          told_naomi = float(max_ken) - 0.0000001
        flag = 1
        while ( flag == 1 ):
          flag = 0
          for i in range(0,len(d_ken)):
            if ( float(ken[i]) == told_naomi ):
              flag = 1
              told_naomi = float(told_naomi - 0.0000001)
        chosen_ken = min(d_ken, key=float)
        case = 0
        for i in range(0,len(d_ken)):
          if ( float(d_ken[i]) > float(told_naomi) and case == 0):
            case = 1
            chosen_ken = d_ken[i]
          elif( float(d_ken[i]) < chosen_ken and float(d_ken[i]) > told_naomi ):
            chosen_ken = d_ken[i]
        d_ken.remove(chosen_ken)

        if ( float(chosen_ken) < float(chosen_naomi) ):
          d_win = d_win + 1

      # simple war
      for x in range(0,blocks):
        chosen_naomi = max( naomi,key=float)
        naomi.remove(chosen_naomi)
        chosen_ken = min(ken, key=float)
        case = 0
        for i in range(0,len(ken)):
          if ( float(ken[i]) > float(chosen_naomi) and case == 0):
            case = 1
            chosen_ken = ken[i]
          elif( float(ken[i]) < chosen_ken and float(ken[i]) > chosen_naomi ):
            chosen_ken = ken[i]
        ken.remove(chosen_ken)
        if ( float(chosen_ken) < float(chosen_naomi) ):
          win = win + 1


      ken[:] = []
      naomi[:] = []
      print d_win,
      print win













  flag = 1
