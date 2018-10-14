for testcase in xrange(1, 1 + input()):
  init, n = map(int, raw_input().split())
  motes = map(int, raw_input().split())
  motes.sort()
  #print init, " - ", motes
  cur = init + sum(m for m in motes if m < init)
  motes = [m for m in motes if m >= init]
  remain = len(motes)
  movs = 0
  if init == 1:
    movs = remain
  else:
    for mote in motes:
      add = 0
      while mote >= cur:
        add += 1
        cur += cur - 1
      if add >= remain:
        movs += remain
        break
      movs += add
      cur += mote
      remain -= 1
  print "Case #%d: %d" % (testcase, movs)
    
