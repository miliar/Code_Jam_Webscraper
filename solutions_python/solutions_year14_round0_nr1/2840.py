# coding: utf-8

import sys

def detect_card():
  f = open(sys.argv[1], 'r')
  f_out = open(sys.argv[1] + '_out', 'w')
  T = int(f.readline()) # the first line
  case = 1

  for i in xrange(T):  
    match = []
    matrix = []
    second_matrix = []
  
    first_answer_row = int(f.readline()) 
    for i in xrange(4):
      row = map(int, f.readline()[:-1].split(' '))
      matrix.append(row)
  
    second_answer_row = int(f.readline()) 
    for i in xrange(4):
      row = map(int, f.readline()[:-1].split(' '))
      second_matrix.append(row)

    print matrix 
    print second_matrix 

    # remember thath the input number starts from 1
    for first_e in matrix[first_answer_row - 1]:
      for second_e in second_matrix[second_answer_row - 1]:
        print first_e, second_e
        if first_e == second_e:
          match.append(first_e)

    output = 'Case #' + str(case) + ': '
    if len(match) == 0:
      output += 'Volunteer cheated!'
    elif len(match) == 1:
      output += str(match[0]) 
    elif len(match) > 1:
      output += 'Bad magician!' 
      
    f_out.write(output + '\n') 
    case += 1

if __name__ == "__main__":
  detect_card()
