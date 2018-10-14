import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
  (n, m) = [int(x) for x in sys.stdin.readline().strip().split()]
  lawn = []
  for j in range(n):
    lawn.append([int(x) for x in sys.stdin.readline().strip().split()])
  max_h = [1] * n
  max_v = [1] * m
  for j in range(n):
    for k in range(m):
      if max_h[j] < lawn[j][k]:
        max_h[j] = lawn[j][k]
      if max_v[k] < lawn[j][k]:
        max_v[k] = lawn[j][k]
  possible = True
  for j in range(n):
    for k in range(m):
      if lawn[j][k] < max_h[j] and lawn[j][k] < max_v[k]:
        possible = False
  print "Case #" + str(i+1) + ": " + ("YES" if possible else "NO")

  def do_lawn_h(lawn, n, m, pos, height):
    for i in range(m):
      if lawn[pos][i] > height:
       lawn[pos][i] = height
  
  def do_lawn_v(lawn, n, m, pos, height):
    for i in range(n):
      if lawn[i][pos] > height:
       lawn[i][pos] = height