def lastTidy(N):
  prev = 0
  ss = list(str(N))
  firstNotTidy = -1
  for i in xrange(1, len(ss)):
    if int(ss[i]) > int(ss[prev]):
      prev = i
    elif int(ss[i]) < int(ss[prev]):
      firstNotTidy = prev
      break

  if firstNotTidy >= 0:
    new = int(ss[firstNotTidy]) - 1
    ss[firstNotTidy] = str(new)
    firstNotTidy += 1
    while firstNotTidy < len(ss):
      ss[firstNotTidy] = '9'
      firstNotTidy += 1
    return int("".join(ss))
  return N


T = input()

for t in xrange(T):
  N = int(raw_input())
  print "Case #" + str(t + 1) + ": " + str(lastTidy(N))

