#!/usr/local/bin/python3
# magic-trick.py

import sys

class Trick():
  def __init__(self, case_number, case_input):
    self.case_number = case_number + 1 
    self.guess1 = int(case_input[0])
    self.guess2 = int(case_input[5])
    self.grid1 = [case_input[1].split(' '),
                  case_input[2].split(' '),
                  case_input[3].split(' '),
                  case_input[4].split(' ')]
    self.grid2 = [case_input[6].split(' '),
                  case_input[7].split(' '),
                  case_input[8].split(' '),
                  case_input[9].split(' ')]

  def evaluate(self):
    firstrow = self.grid1[self.guess1 - 1]
    secondrow = self.grid2[self.guess2 - 1]
    cards = set(firstrow) & set(secondrow)
    if (len(cards) == 0):
      print('Case #' + str(self.case_number) + ': Volunteer cheated!')
    elif(len(cards) == 1):
      print('Case #' + str(self.case_number) + ': ' + cards.pop())
    else:
      print('Case #' + str(self.case_number) + ': Bad magician!')

if __name__ == "__main__":
  input = open(sys.argv[1], 'r')
  num_cases = input.readline()  

  case_lines = []
  for line in input.readlines():
    case_lines.append(line.strip('\n'))
  
  tricks = []
  for i in range(int(num_cases)):
    single_case = []
    for j in range(10):
      single_case.append(case_lines[(10 * i) + j])
    trick = Trick(i, single_case)
    tricks.append(trick)

  for t in tricks:
    t.evaluate() 
