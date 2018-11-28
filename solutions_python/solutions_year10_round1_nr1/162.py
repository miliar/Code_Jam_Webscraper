import numpy as N
import pdb

def code_jam():
  #input_filename = 'test.txt'
  #input_filename = 'A-small-attempt0.in'
  input_filename = 'A-large.in'
  input_file = open(input_filename)
  output_file = open(''.join(('output_',input_filename)), 'w')
  num_cases = int(input_file.readline())

  for case_number in xrange(num_cases):
    print 'starting case ' + str(case_number+1)
    line  = input_file.readline()
    line_size, winning_length = map(int, line.split())
    array = N.empty((line_size,line_size),int)

    # read in the array
    for y in xrange(line_size):
      line = input_file.readline()
      for x in xrange(line_size):
        char = line[x]
        if char == '.':
          i = 0
        if char == 'B':
          i = 1
        if char == 'R':
          i = 2
        array[x,y] = i

    # rotate the array
    for y in xrange(line_size):
      first_dot = line_size-1
      for x in range(line_size)[::-1]:
        if array[x,y] <> 0:
          temp = array[first_dot, y]
          array[first_dot, y] = array[x,y]
          array[x,y] = temp
          first_dot -= 1

    # helper functions
    def match_down(x,y,element):
      for i in xrange(1, winning_length):
        if (x+i > line_size-1):
          return False
        if array[x+i,y] <> element:
          return False
      return True

    def match_downleft(x,y,element):
      for i in xrange(1, winning_length):
        if (x+i > line_size-1):
          return False
        if (y+i > line_size-1):
          return False
        if array[x+i,y+i] <> element:
          return False
      return True

    def match_left(x,y,element):
      for i in xrange(1, winning_length):
        if (y+i > line_size-1):
          return False
        if array[x,y+i] <> element:
          return False
      return True

    def match_upleft(x,y,element):
      for i in xrange(1, winning_length):
        if (x-i < 0):
          return False
        if (y+i > line_size-1):
          return False
        if array[x-i,y+i] <> element:
          return False
      return True

    # check for matches
    won = [0,0,0]
    for y in xrange(line_size):
      for x in xrange(line_size):
        element = array[x,y]
        if element == 0:
          continue
        if match_down(x,y,element):
          won[element] = 1
        if match_downleft(x,y,element):
          won[element] = 1
        if match_left(x,y,element):
          won[element] = 1
        if match_upleft(x,y,element):
          won[element] = 1

    print won
    if (won[1]==0 and won[2]==0):
      state = 'Neither'
    if (won[1]==1 and won[2]==0):
      state = 'Blue'
    if (won[1]==0 and won[2]==1):
      state = 'Red'
    if (won[1]==1 and won[2]==1):
      state = 'Both'
    string = 'Case #' + str(case_number+1) + ': ' + state + '\n'
    output_file.write(string)



  output_file.close()
  input_file.close()

code_jam()
