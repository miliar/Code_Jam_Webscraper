
f1 = open("input.txt", "r")
f2 = open("out.txt", "w+")
numCases = int(f1.readline())

for i in range(numCases):
  nums = map(float, f1.readline().split())
  fCost = nums[0]
  fProd = nums[1]
  goal = nums[2]
  curRate = 2.0
  reachedGoal = False;
  time = 0.0
  while(not reachedGoal):
    TTF = fCost / curRate
    TTG = goal / curRate
    TWFTG =  goal / (curRate+fProd) + TTF
    if TTG <= TWFTG:
      time += TTG
      reachedGoal = True
    else:
      time += TTF
      curRate += fProd
  f2.write("Case #{}: {}\n".format(i+1, time))
