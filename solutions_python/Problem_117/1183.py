import sys

def IN():
  return sys.stdin.readline()

def OUT(txt):
  ERR("[OUT] " + txt)
  sys.stdout.write(txt)
  sys.stdout.flush()

def ERR(txt):
  print >> sys.stderr, txt

ERR("start")

def do_case(num):
  OUT("Case #" + str(num + 1) + ": ")
  n, m = (int(x) for x in IN().split())
  ERR("%d %d" % (n, m))
  lawn = tuple(tuple(int(x) for x in IN().split()) for _ in range(n))
  ERR(lawn)
  for h in range(1, 101):
    for x in range(n):
      for y in range(m):
        if h == lawn[x][y]:
          if (all(lawn[t][y] <= h for t in range(0, n)) or
              all(lawn[x][t] <= h for t in range(0, m))):
            pass
          else:
            OUT("NO\n")
            return
  OUT("YES\n")


for case in range(int(IN())):
  do_case(case)

sys.stdout.flush()
