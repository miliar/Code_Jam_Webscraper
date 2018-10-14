def work():
  n, _ = map(int, input().split(" "))
  e = []
  s = []
  for i in range(n):
    x, y = map(int, input().split(" "))
    e.append(x)
    s.append(y)
  d = []
  d.append(0)
  for i in range(n):
    x = list(map(int, input().split(" ")))
    for j in range(n):
      if i + 1 == j:
        d.append(d[i] + x[j])
  _, _ = map(int, input().split(" "))

  best = [1e18] * n
  best[n - 1] = 0
  for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
      if d[j] - d[i] <= e[i]:
        best[i] = min(best[i], best[j] + (d[j] - d[i]) / s[i])
  return best[0]


if __name__ == '__main__':
  tc = int(input())
  for cc in range(1, tc + 1):
    print('Case #%d: %.6f' % (cc, work()))
