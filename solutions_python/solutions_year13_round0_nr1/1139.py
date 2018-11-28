import sys
import re

inp = open(sys.argv[1])
out = open(sys.argv[1].replace(".in",".out"), "w")

x_win = re.compile('(X|T){4}')
y_win = re.compile('(O|T){4}')

def parse(case, str_array):
  finished = True
  horizontal = []
  vertical = ['', '', '', '']
  diagonal = []

  for line in str_array:
    horizontal.append(line)
    for pos in range(len(line)):
      vertical[pos] += line[pos]

  diagonal.append(str_array[0][0] + str_array[1][1] + str_array[2][2] + str_array[3][3])
  diagonal.append(str_array[0][3] + str_array[1][2] + str_array[2][1] + str_array[3][0])

  check = horizontal + vertical + diagonal
  for row in check:
    if '.' in row:
      finished = False
    if x_win.match(row):
      return "Case #%d: X won\n"%case
    elif y_win.match(row):
      return "Case #%d: O won\n"%case

  if finished:
    return "Case #%d: Draw\n"%case
  else:
    return "Case #%d: Game has not completed\n"%case

cases = int(inp.readline().strip())
for i in range(cases):
  str_array = []
  for j in range(4):
    str_array.append(inp.readline().strip())
  inp.readline()
  #out.write(parse(i, str_array))
  out.write(parse(i+1, str_array))
  

  
  
