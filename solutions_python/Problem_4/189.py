for case in range(input()):
  input()
  xs = sorted(map(int, raw_input().split()), key=abs, reverse=1)
  ys = map(int, raw_input().split())
  sp = 0
  for x in xs:
    if x >= 0:
      y = min(ys)
    else:
      y = max(ys)

    ys.remove(y)
    sp += x * y

  print 'Case #%d: %d' % (case + 1, sp)
