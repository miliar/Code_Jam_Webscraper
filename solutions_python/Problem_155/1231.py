
def main():
  dbg = False
  #f = open('A-sample.txt', 'r')
  #f = open('A-small-attempt0.in', 'r')
  f = open('A-large.in', 'r')
  data = f.readlines()
  T = int(data[0])
  case = 1
  line = 1
  while case <= T:
    smax,ni = data[line].split()
    smax = int(smax)
    line += 1

    if (dbg): print "============================================"
    if (dbg): print smax, ni
    if (dbg): print "============================================"

    # First is special, there needs to be someone with si=0 to start the chain
    added = 0
    up    = 0
    n     = int(ni[0])
    if n == 0:
      added = 1
    up = n + added

    # Then for each rank X where there is at least one person with si=X,
    # we need to have enough people who got up before
    for x in xrange(1,smax+1):
      n = int(ni[x])
      if n == 0:
        continue
      px = max(0, x-up)
      up = up + n + px
      added = added + px

    solution = added

    print "Case #%d: %s" % (case, solution)
    case += 1

if __name__ == "__main__":
    main()
