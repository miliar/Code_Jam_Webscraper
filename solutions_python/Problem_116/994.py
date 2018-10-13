import re
import string

input =  open("Qualification/A-large.in")
output = open("Qualification/A-large.out", 'w')

def read_table(input):
  table = []
  for i in range(4):
    table.append(input.readline()[:-1])
  input.readline() # blank line

  for i in range(4):
    table.append(string.join([table[x][i] for x in range(4)], ""))
  table.append(string.join([table[x][x] for x in range(4)], ""))
  table.append(string.join([table[3-x][x] for x in range(4)], ""))
  return table

def find_winner(table):
  t = string.join(table)
  if re.search("[XT][XT][XT][XT]", t) <> None:
    return "X won"
  elif re.search("[OT][OT][OT][OT]", t) <> None:
    return "O won"
  elif re.search("\.", t) <> None:
    return "Game has not completed"
  else:
    return "Draw"

T = int(input.readline())
for t in range(T):
  print "case",t
  table = read_table(input)
  result = find_winner(table)
  output.write("Case #{0}: {1}\n".format(t+1, result))

output.flush()
input.close()
output.close()

