def other(r):
  return 1-r

def sign(n):
  if n >= 0:
    return 1
  return -1

for case in xrange(1, int(raw_input())+1):
  line = raw_input().split()
  N = int(line[0])
  A = zip(line[1::2], map(int, line[2::2]))
  p = [1,1]
  r = {'O':0,'B':1}
  ans = 0
  for i, a in enumerate(A):
    robot = r[a[0]]
    moves = abs(p[robot] - a[1]) + 1
    p[robot] = a[1]
    other_robot = other(robot)
    found = False
    for j, other_a in enumerate(A[i+1:]):
      if r[other_a[0]] == other_robot:
        found = True
        break
    ans += moves
    if found:
      max_moves = abs(p[other_robot] - other_a[1])
      if max_moves > moves:
        dir = -sign(p[other_robot] - other_a[1])
        p[other_robot] += dir * moves
      else:
        p[other_robot] = other_a[1]
  print "Case #%d: %d" % (case, ans)
