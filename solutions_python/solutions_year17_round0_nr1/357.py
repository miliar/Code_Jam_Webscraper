

testnum = int(input())
for i in range(1, testnum+1):
  panrow, flipsize = input().split(" ")
  panrow = [x=='+' for x in list(panrow)]
  flipsize = int(flipsize)
  
  if (flipsize == 1):
    flipsize = sum(not x for x in panrow)
    print("Case #"+str(i)+": "+str(flipsize))
  
  else:
    flipnum = 0
    for j in range(len(panrow)):
      if j+flipsize <= len(panrow) and  not panrow[j]:
        panrow[j:j+flipsize] = [not x for x in panrow[j:j+flipsize]]
        flipnum += 1
        
    if panrow[len(panrow)-flipsize:] == [True]*flipsize:
      print("Case #"+str(i)+": "+str(flipnum))
    else:
      print("Case #"+str(i)+": IMPOSSIBLE")