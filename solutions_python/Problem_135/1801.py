#!/usr/bin/python

import sys
import copy 

input_file = open(sys.argv[1], "r")

file_line = 0
card_line = 1
number = -1
stored_line = [0,1,2,3]
stored_line2 = [0,1,2,3]
case = 0

for line in input_file:
  token = line.split()
  if file_line == 0:
    test_cases = token[0]
    file_line = file_line + 1
  elif file_line == 1:
    first_guess = int(token[0])
    file_line = file_line + 1
  elif file_line == 2:
    if first_guess == card_line:
      stored_line = copy.deepcopy(token)
    card_line = card_line + 1
    if card_line == 5:
      file_line = file_line + 1
      card_line = 1
  elif file_line == 3:
    second_guess = int(token[0])
    file_line = file_line + 1
  elif file_line == 4:
    if second_guess == card_line:
      stored_line2 = copy.deepcopy(token)
    card_line = card_line + 1
    if card_line == 5:
      file_line = 1
      card_line = 1
      flag = 0
      for x in range(0,4):
        for y in range(0,4):
          if int(stored_line[x]) == int(stored_line2[y]):
            number = stored_line[x]
            flag = flag + 1
      case = case + 1
      if flag == 0:
        print ("Case #{0}: Volunteer cheated!".format(case))
      elif flag == 1:
        print ("Case #{0}: {1}".format(case,number))
      else:
        print ("Case #{0}: Bad magician!".format(case))

