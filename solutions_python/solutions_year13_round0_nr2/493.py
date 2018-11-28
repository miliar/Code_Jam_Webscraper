import sys

def is_bad_case_at(x, y, lawn):
  target = lawn[x][y]
  if (x > 0):
    if (y > 0):
      if (target < lawn[x - 1][y] and target < lawn[x][y - 1]):
        return 1
    if (y < len(lawn[0]) - 1):
      if (target < lawn[x - 1][y] and target < lawn[x][y + 1]):
        return 1
  if (x < len(lawn) - 1):
    if (y > 0):
      if (target < lawn[x + 1][y] and target < lawn[x][y - 1]):
        return 1
    if (y < len(lawn[0]) - 1):
      if (target < lawn[x + 1][y] and target < lawn[x][y + 1]):
        return 1
  return 0
  
def is_bad_case_at2(x, y, lawn, highest_in_rows, highest_in_cols):
  target = lawn[x][y]
  return (highest_in_rows[y] > target and highest_in_cols[x] > target)
  
def run_case(infile):
  line = [int(v) for v in infile.readline().split()]
  N = line[0]
  M = line[1]
  
  lawn = []
  
  for n in range(N):
    line = [int(v) for v in infile.readline().split()]
    lawn_row = []
    lawn.append(lawn_row)
    for m in range(M):
      lawn_row.append(line[m])
      
  highest_in_rows = []
  for y in range(M):
    highest_in_rows.append(0)
  highest_in_cols = []
  for x in range(N):
    highest_in_cols.append(0)
  
  for y in range(M):
    for x in range(N):
      target = lawn[x][y]
      highest_in_rows[y] = max(highest_in_rows[y], target)
      highest_in_cols[x] = max(highest_in_cols[x], target)
  
  for y in range(M):
    for x in range(N):
      if (is_bad_case_at2(x, y, lawn, highest_in_rows, highest_in_cols)):
        return "NO"
  
  return "YES"

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  print run_case(infile)
  
infile.close() 