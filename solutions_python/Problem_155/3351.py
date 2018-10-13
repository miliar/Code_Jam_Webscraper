
def getMaxFriends(maxS, vals):
  index = 0
  numStanding = 0
  friends = 0
  for i in xrange(len(vals)):
    if numStanding >= i:
      numStanding += int(vals[i])
    else:
      friends += (i - numStanding)
      numStanding = i + int(vals[i])
  return friends

def win():
  f = open("A-large.in", 'r')
  stuff = f.read().splitlines()[1:]
  answers = []
  for (i, line) in enumerate(stuff):
    maxS, vals = line.split()
    friends = getMaxFriends(maxS, vals)
    answers.append("Case #%d: %d" % (i + 1, friends))
  for answer in answers:
    print answer

win()