for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  A1 = input()
  for r in xrange(4):
    inp = raw_input()
    if r+1 == A1:
      choice1 = set(map(int, inp.split()))
  A2 = input()
  for r in xrange(4):
    inp = raw_input()
    if r+1 == A2:
      choice2 = set(map(int, inp.split()))
  common = choice1 & choice2
  if not common:
    print "Volunteer cheated!"
  elif len(common) > 1:
    print "Bad magician!"
  else:
    print common.pop()
