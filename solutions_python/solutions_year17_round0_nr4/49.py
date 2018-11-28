

def rooks(SIZE, coords):
  o_cols = set(x for x,y in coords)
  o_rows = set(y for x,y in coords)
  f_cols = [i for i in range(1, 1+SIZE) if i not in o_cols]
  f_rows = [i for i in range(1, 1+SIZE) if i not in o_rows]
  return zip(f_cols, f_rows)
  
def bishops(SIZE, coords):
  o_subs = set(x - y for x,y in coords)
  o_adds = set(x + y for x,y in coords)
  def foo(x, y):
    xyadd = x + y
    xysub = x - y
    if (xyadd not in o_adds) and (xysub not in o_subs):
      o_adds.add(xyadd)
      o_subs.add(xysub)
      yield (x, y)
  xmin, xmax = 1, SIZE
  while xmin <= xmax:
    for i in range(xmin, xmax):
      yield from foo(i, xmin)
      yield from foo(xmax, i)
      yield from foo(SIZE - i + 1, xmax)
      yield from foo(xmin, SIZE - i + 1)
    xmax -= 1
    xmin += 1
  if SIZE % 2 == 1:
    yield from foo(SIZE // 2 + 1, SIZE // 2 + 1)


def testcase(CASE):
  SIZE, cnt = map(int, input().split())
  data = []
  for _ in range(cnt):
    parts = input().split()
    data.append((int(parts[1]), int(parts[2]), parts[0]))
  ixs = [d[:2] for d in data if d[2] in "xo"]
  nxs = set(rooks(SIZE, ixs))
  ips = [d[:2] for d in data if d[2] in "+o"]
  nps = set(bishops(SIZE, ips))
  aps = nps.union(ips)
  axs = nxs.union(ixs)
  
  outp = [(".x+o"[int(p in axs) + 2 * int(p in aps)], *p) for p in nxs.union(nps)]
  
  print("Case #{}: {} {}".format(CASE, 
    len(aps) + len(axs),
    len(outp)
  ))
  for row in outp:
    print(" ".join(map(str, row)))
  
T = int(input())
for i in range(T):
  testcase(i + 1)
