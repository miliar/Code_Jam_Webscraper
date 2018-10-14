import sys
f = open('B-large.in', 'r+')
output = open('cookiesOutput.txt', 'w+')
numberOfCase = int(f.readline())

for case in range(1, numberOfCase + 1):
  line = f.readline().split(' ')
  C = float(line[0])
  F = float(line[1])
  X = float(line[2])
  
  currentTime = 0
  prod = 2
  
  continuing = True
  minTimeToWin = sys.maxint
  while continuing:
    timeToWin = X / prod
    timeNextFarm = C / prod
    currentTimeToWin = currentTime + timeToWin
    if minTimeToWin > currentTimeToWin:
      minTimeToWin = currentTimeToWin
      currentTime += timeNextFarm
      prod += F
    else:
      continuing = False

  out =  "Case #" + str(case) + ": " + str(round(minTimeToWin, 7)) + "\n"
  output.write(out)
  print out,


  
  

  
  