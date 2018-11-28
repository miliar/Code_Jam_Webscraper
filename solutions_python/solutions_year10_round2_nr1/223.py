T = int(raw_input())

def add(root, dir, new):
  if not dir:
    return
  if dir[0] not in root:
    root[dir[0]] = ({}, new)
  add(root[dir[0]][0], dir[1:], new)

def count_new(root):
  ans = 0
  for name in root:
    folders = root[name][0]
    new = root[name][1]
    if new:
      ans += 1
    ans += count_new(folders)
  return ans

for case in xrange(1, T+1):
  N, M = map(int, raw_input().split())

  root = {}

  for i in xrange(N):
    dir = raw_input().strip().split(r"/")
    add(root, dir[1:], False)
  for i in xrange(M):
    dir = raw_input().strip().split(r"/")
    add(root, dir[1:], True)

  ans = count_new(root)
  print "Case #%d: %d" % (case, ans)

