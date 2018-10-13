def change(_ps, _k):
  for i in range(0, len(_ps)):
    if i < _k:
      _ps[i] = not _ps[i]
  return _ps

def changeAll(_ps, _k, cnt):
    if len(_ps) < _k:
        return cnt if all(_ps) else "IMPOSSIBLE"

    if not _ps[0]:
        changed = change(_ps, _k)
        return changeAll(changed[1:], _k, cnt+1)

    return changeAll(_ps[1:], _k, cnt)

t = int(raw_input())
for i in xrange(1, t + 1):
  _ps, _k = [s for s in raw_input().split(" ")]
  print "Case #" + str(i) + ": " + str(changeAll(map(lambda x: x == '+', list(_ps)), int(_k), 0))
