cases = int(input())

for c in xrange(cases):
  line = int(input()) - 1
  numbers1 = None
  numbers2 = None
  for x in xrange(4):
    if x == line:
      numbers1 = raw_input().split()
    else:
      raw_input()
  line = int(raw_input()) - 1
  for x in xrange(4):
    if x == line:
      numbers2 = raw_input().split()
    else:
      raw_input()
  both = set(numbers1) & set(numbers2)
  if len(both) > 1:
    print "Case #" + str(c + 1) + ": Bad magician!"
  elif len(both) == 1:
    print "Case #" + str(c + 1) + ": " + both.pop()
  else:
    print "Case #" + str(c + 1) + ": Volunteer cheated!"
