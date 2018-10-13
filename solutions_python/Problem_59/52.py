def gen_dirs(dir):
  d = ""
  for subdir in dir.split("/")[1:]:
    d += "/" + subdir
    yield d

for case in xrange(1, int(raw_input())+1):
  N, M = map(int, raw_input().split())
  dirs = set()
  for _ in xrange(N):
    for dir in gen_dirs(raw_input()):
      dirs.add(dir)
  ans = 0
  for _ in xrange(M):
    for dir in gen_dirs(raw_input()):
      if dir not in dirs:
        dirs.add(dir)
        ans += 1
  print "Case #%d: %d" % (case, ans)
