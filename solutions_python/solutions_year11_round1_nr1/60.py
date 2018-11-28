#! /usr/bin/python2

def main():
  # read in number of test cases
  ntc = int(raw_input())
  for c in range(ntc):
    # read in N and K
    words = raw_input().split(None)
    N = int(words[0])
    PD = int(words[1])
    PG = int(words[2])
    works = "Possible"
    if (PD < 0 or PD > 100):
      works = "Broken"
    if (PG < 0 or PG > 100):
      works = "Broken"
    if (PG == 0 and PD > 0):
      works = "Broken"
    if (PG == 100 and PD < 100):
      works = "Broken"
    canDivide = False
    for i in range(min(N,100)):
      games = (i+1) * PD / 100.0
      if (games == int(games)):
        canDivide = True
    # we are done and can output the result for the test case
    if (not canDivide):
      works = "Broken"
    print "Case #{0}: {1}".format(c+1, works);

if __name__ == '__main__':
  main()
