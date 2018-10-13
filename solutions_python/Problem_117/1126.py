# lawnmower.py
import sys

def rotate_lawn(lawn):
  new_lawn = []
  return new_lawn

def is_lawn_valid(lawn):
  for row in range(len(lawn)):
    for col in range(len(lawn[row])):
      if col <= 0  or max(lawn[row][:col]) <= lawn[row][col]:
        if col >= len(lawn[row])-1 or max(lawn[row][col+1:]) <= lawn[row][col]: continue
      if row == 0 or max([lawn[x][col] for x in range(row)]) <= lawn[row][col]:
        if row == len(lawn)-1 or max([lawn[row+x][col] for x in range(len(lawn)-row)[1:]]) <= lawn[row][col]: continue
      return 'NO'
  return 'YES'

if __name__ == '__main__':
  N = int(sys.stdin.readline().strip())
  
  for i in range(N):
    row_col_line = sys.stdin.readline().strip()
    rows = int(row_col_line.split()[0])
    cols = int(row_col_line.split()[1])
    lawn = []
    for j in range(rows):
      line = sys.stdin.readline().strip()
      lawn.append([int(x) for x in line.split()])
    print 'Case #'+str(i+1)+': '+str(is_lawn_valid(lawn))
    
