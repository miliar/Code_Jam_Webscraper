import sys

with sys.stdin as f:
  numLines = int(next(f))
  case = 1
  for l in range(numLines):
    d = map(int, next(f).strip().split()[1])
    nPeople = 0 # number of people
    iPeople = 0 # current index
    dPeople = 0 # difference required
    for n in d:
      if nPeople < iPeople:
        dPeople += (iPeople - nPeople)
        nPeople = iPeople
      nPeople += n
      iPeople += 1
    print "Case #{}: {}".format(case, dPeople)
    case += 1