#! /usr/bin/python3

def main(inFileName):
  with open(inFileName, 'r') as inFile:
    T = int(inFile.readline())
    for t in range(T):
      C, F, X = inFile.readline().split()
      C = float(C)
      F = float(F)
      X = float(X)
      seconds = algo(C, F, X)
      print("Case #{0}: {1:.7f}".format(t+1, seconds))    

def algo(C, F, X):
  seconds = 0.0
  cookies = 0
  rate = 2

  while cookies < X:
    # should I buy a farm, or should I wait
    timetofarm = C / rate
    timetofinish = X / rate
    timetofinishwithfarm = timetofarm + (X / (rate + F))

    if X < C:
      seconds = seconds + timetofinish
      return seconds

    if timetofinish < timetofinishwithfarm:
      seconds = seconds + timetofinish
      return seconds
    else:
      #buy a farm
      seconds = seconds + timetofarm
      cookies = 0
      rate = rate + F

  return seconds

if __name__ == "__main__":
  import sys
  if len(sys.argv) == 2:
    main(sys.argv[1])
