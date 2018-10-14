def solve(ct, up, prev):
  global n

  if ct == len(n):
    return "", 0

  for i in range(9, -1, -1):
    if i < prev:
      continue
    if not(up) and i > int(n[ct]):
      continue

    if i < int(n[ct]):
      ans, nm = solve(ct + 1, True, i)
    else:
      ans, nm = solve(ct + 1, up, i)

    if nm >= 0:
      return str(i) + ans, nm + 1
  return "", -1

t = int(raw_input())

for i in range(t):
  n = raw_input()
  ans,_ = solve(0, False, 0)

  print "Case #%d: %d" % (i + 1, int(ans))
