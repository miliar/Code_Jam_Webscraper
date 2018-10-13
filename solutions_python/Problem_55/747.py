
numCases = int(raw_input())
for c in xrange(numCases):
   r, k, _ = map(int, raw_input().split())
   nums = map(int, raw_input().split())
   
   seenCur = [False]*len(nums)
   
   rides = 0
   money = 0

   curPlace = 0
   curSum = 0
   while True:
      if curSum + nums[curPlace] > k or seenCur[curPlace]:
         money += curSum
         curSum = 0
         
         seenCur = [False]*len(nums)
      
         rides += 1
         if rides >= r:
            break
   
      curSum += nums[curPlace]
      seenCur[curPlace] = True
   
      curPlace = (curPlace + 1) % len(nums)
   
   print "Case #%d: %d" % (c+1, money)
      
