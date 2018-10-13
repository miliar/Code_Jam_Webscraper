import sys
import math

def min_height(lawn):
  minimum = 101
  for row in lawn:
    for col in row:
      minimum = min(minimum, int(col))
  return minimum

def cut_lawn(lawn):
  changed = True
  while len(lawn) != 0:
    if not changed:
      return False
    changed = False
    minimum = min_height(lawn)
    for row in lawn:
      if row.count(str(minimum)) == len(row):
        lawn.remove(row)
        changed = True
        break
    else:
      for i in range(0,len(lawn[0])):
        column = ""
        for j in range(0,len(lawn)):
          column += lawn[j][i]
        if column.count(str(minimum)) == len(lawn):
          for row in lawn:
            row.pop(i)
          changed = True
          break
  return True

num_problems = int(sys.stdin.readline())
for i in range(0,num_problems):
  row_col = sys.stdin.readline().split()
  lawn = []
  for j in range(0, int(row_col[0])):
    lawn.append(sys.stdin.readline().split())
  if cut_lawn(lawn):
    print "Case #" + str(i+1) + ": YES" 
  else:
    print "Case #" + str(i+1) + ": NO" 


