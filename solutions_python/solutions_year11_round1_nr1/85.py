import sys, math

def solvecase(N, PD, PG):
  #D, G such that WD = PD*D and WG=
  if PD < PG and PG == 100:
    return "Broken"

  if PD > 0 and PG == 0:
    return "Broken"

  if N > 100:
    return "Possible"

  for i in range(1,N+1):
    if PD*i % 100 == 0:
      return "Possible"

  return "Broken"

def parsecase():
  N, PD, PG = [int(a) for a in sys.stdin.readline().strip().split(" ") ]
  return solvecase(N, PD, PG)

def parsecases():
  t = sys.stdin.readline().strip()
  t = int(t)
  return t

def main():
  cases = parsecases()
  i = 1
  while i <= cases:
    print "Case #%s: %s" % (i, parsecase() )
    i += 1

if __name__ == "__main__":
    main()
