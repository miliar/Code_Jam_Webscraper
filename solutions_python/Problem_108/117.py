for _ in xrange(1, int(raw_input()) + 1):
  print "Case #%d:" % (_),
  N = int(raw_input())
  a = []
  for n in xrange(N):
    a.append([int(x) for x in raw_input().split()])
  D = int(raw_input())
  cur, reach = 0, a[0][0] * 2
  flag = 0
  checked = [0] * N

  def dfs(p, r):
    global flag
    global checked
    global D
    if r >= D:
      flag = 1
      return
    if r <= checked[p]:
      return
    checked[p] = r
    for i in xrange(p + 1, N):
      if a[i][0] > r: return
      t_reach = a[i][0] + min(a[i][1], a[i][0] - a[p][0])
      if t_reach >= D:
        flag = 1
      else:
        dfs(i, t_reach)
      if flag: return

  dfs(cur, reach)

  print "YES" if flag else "NO"
