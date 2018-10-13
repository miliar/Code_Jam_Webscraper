
def where_meet(l1, s1, l2, s2, dist):
  if s1 == s2:
    return dist + 1
  time = (1.0*(l2-l1)) / (s1-s2)
  if time < 0:
    return dist + 1
  return l1 + time * s1

def calculate(array, total):
  time = None
  for start, speed in array:
    curtime = (total - start)*1.0 / speed
    if time == None:
      time = curtime
      continue
    time = max(curtime, time)
  return total / time

cases = int(raw_input())
for i in xrange(1, cases+1):
  total, n = map(int, raw_input().split(' '))
  array = []
  for j in xrange(n):
    start, speed = map(int, raw_input().split(' '))
    array.append([start, speed])
  speed = calculate(array, total)
  print "Case #%d: %f" % (i, speed)
