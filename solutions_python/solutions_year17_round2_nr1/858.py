num = int(input())  # read a line with a single integer


for i in range(1, num + 1):
  stravel, snumhorse = input().split() 
  travel, numhorse = float(stravel), int(snumhorse)
  maxtime = ~1
  for x in range (numhorse):
    spos, sspeed = input().split()
    pos, speed = float(spos), float (sspeed)
    time = ((travel-pos)/speed)
    if time > maxtime:
        maxtime = time
  out = travel/maxtime
  print("Case #{}: {}".format(i,out))
