def parseInputFrom(line):
  return int(line.split(" ")[0]), int(line.split(" ")[1])

def helper(l, k):
  res = []
  m, M = 0, 0
  for A, n in l:
    if k > 0:
      A -= 1
      m = A // 2
      M = A - m
      if len(res) > 0 and res[-1][0] == M:
        res[-1][1] += n
      else:
        res.append([M, n])

      if res[-1][0] == m:
        res[-1][1] += n
      else:
        res.append([m, n])
      k -= n
    else:
      return M, m
  if k <= 0:
    return M, m
  return helper(res, k)

def solve(N, K):
  return helper([[N, 1]], K)

def represent(i, res):
  return "Case #"+str(i)+": "+("IMPOSSIBLE" if res is None else str(res[0]) + " " + str(res[1]))

with open("input.in") as f:
  with open("output.out", "w") as f2:
    n = int(f.readline())
    i = 1
    line = f.readline()
    while line and i <= n:
      print(i, "/", n)
      N, K = parseInputFrom(line)
      res = solve(N, K)
      f2.write(represent(i, res)+"\n")
      i += 1
      line = f.readline()
