def solve(N, M, lawn):
  height = []
  for n in range(N):
    for m in range(M):
      lawn[n][m] = int(lawn[n][m])
      h = lawn[n][m]
      if h not in height:
        height.append(h)
  height.sort(reverse = True) 

  for h in height:
    b_lawn = []
    for n in range(N):
      b_lawn.append([])
      for m in range(M):
        if lawn[n][m] <= h:
          b_lawn[n].append(1)
        else:
          b_lawn[n].append(0)
    if solve_b_lawn(N, M, b_lawn):
      return "NO"
    
  return "YES"

def solve_b_lawn(N, M, b_lawn):
  for n in range(N):
    for m in range(M):
      if b_lawn[n][m] == 1:
        if 0 in b_lawn[n] and 0 in [row[m] for row in b_lawn]:
          return True
  return False

File = open("B-large.in", "r")
f = []
for line in File:
  f.append(line.split())
row = 1
for i in range(int(f[0][0])):
  N = int(f[row][0])
  M = int(f[row][1])
  print "Case #%d:" %(i+1), solve(N, M, f[row + 1 : row + 1 + N])
  row = row + 1 + N