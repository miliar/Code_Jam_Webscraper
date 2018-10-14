def trac(C, F, X, FC):
  goalTime = (X * 1.0/ ((F * FC) + 2))
  withNewFarm = ((X)* 1.0 / ((F * (FC + 1)) + 2))
  newFarmTime = ((C)* 1.0 / ((F * (FC)) + 2));
  if goalTime > withNewFarm + newFarmTime:
    return (True, newFarmTime)
  else:
    return (False, goalTime);

T = int(input())

for i in range(0, T):
  (C, F, X) = map(float, raw_input().split(" "))
  total = 0;
  farmCount = 0
  while(1):
    (cont, time) = trac(C, F, X, farmCount)
    total += time
    if not cont:
      break;
    farmCount += 1
  print "Case #%d: %.7f" % (i+1, total)

