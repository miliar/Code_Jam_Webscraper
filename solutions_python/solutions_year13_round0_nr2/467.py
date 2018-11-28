get_ints = lambda: map(int, raw_input().split())
for i in range(1, input()+1):
  rows, cols = get_ints()
  a = [get_ints() for j in range(rows)]
  v = [[False]*cols for r in range(rows)]
  for r, row in enumerate(a):
    m = max(row)
    for c, col in enumerate(row):
      if col == m: v[r][c] = True
  for c in range(cols):
    m = a[0][c]
    for r in range(rows): m = max(m, a[r][c])
    for r in range(rows):
      if a[r][c] == m: v[r][c] = True
  if all(map(all, v)): ans = 'YES'
  else: ans = 'NO'
  print 'Case #%i:'%i, ans
