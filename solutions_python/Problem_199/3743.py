t = int(input()) # read a line with a single integer
for i in range(1, t+1):
  n, m = [str(s) for s in input().split(" ")] 
  flipNum=int(m)
  pancakes = list(n)
  numPancakes = len(pancakes)

  flips=0
  idx = 0
  while idx < numPancakes:
    if pancakes[idx] == "+":
      idx= idx + 1
    else:
      # flip next few pancakes if possible
      flipBegin = idx
      flipEnd = idx+flipNum
      if (flipEnd <= numPancakes):
        #flip
        flips=flips+1
        for y in range (flipBegin, flipEnd):
          if pancakes[y] == "+":
            pancakes[y] = "-"
          elif pancakes[y] == "-":
            pancakes[y] = "+"
        idx = idx+1
      else:
        flips = -1   # Negative implies impossible here
        idx = numPancakes
  # end while
  if (flips >= 0):
    print("Case #{}: {} ".format(i, flips))
  else:
    print("Case #{}: {} ".format(i, "IMPOSSIBLE"))
    

