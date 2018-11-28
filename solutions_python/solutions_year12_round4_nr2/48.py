import sys

def find_next(ans, R, W, L, old_y):
  max_y = R + max(map(lambda x: x[1] + x[2][0], ans))
  min_y = max_y
  min_x = 0

  for i in xrange(len(ans)):
    if ans[i][1] == old_y:
      new_y = ans[i][1] + ans[i][2][0] + R
      if min_y > new_y:
        min_y = new_y
        min_x = ans[i][0]
  return (min_x, min_y)

def solve(inpf):
  line = inpf.readline()
  tokens = map(long, line.strip().split())
  N = tokens[0]
  W = tokens[1]
  L = tokens[2]

  tokens = map(long, inpf.readline().split())
  radius = []
  for i in xrange(len(tokens)):
    radius.append((-tokens[i], i))
  radius = map(lambda x: (-x[0], x[1]), sorted(radius))
  
  ans = []
 
  x = -radius[0][0]
  y = 0
  
  for i in xrange(len(radius)):
    x += radius[i][0]
    if x <= W and y <= L:
      ans.append((x, y, radius[i]))
      x += radius[i][0]
    else:
      (x, y) = find_next(ans, radius[i][0], W, L, y)
      ans.append((x, y, radius[i]))
      x += radius[i][0]
  ans = map(lambda x: (x[1], x[2]), sorted(map(lambda x: (x[2][1], x[0], x[1]), ans) ) )
  return ' '.join(map(lambda x: str(x[0]) + ' ' + str(x[1]), ans))

if len(sys.argv) < 2: 
  print 'Usage: python *.py [input_file]'
  exit(-1)

inpf = open(sys.argv[1], 'r')

N = int(inpf.readline().strip())

for i in xrange(N):
  ans = solve(inpf)
  print 'Case #' + str(i+1) + ': ' + ans
inpf.close()
