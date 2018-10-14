t = int(raw_input())
for caseNum in range(t):
   height, width = map(int, raw_input().split())
   grid = [[False for x in range(width)] for y in range(height)]
   used = [[False for x in range(width)] for y in range(height)]
   
   for y in range(height):
      row = int(raw_input(), 16)
      row_b = map(bool, map(int, list(bin(row)[2:])))
      row_b = [False for i in range(width-len(row_b))] + row_b
      #print row_b
      for x, v in enumerate(row_b):
         grid[y][x] = v
   
   counts = [0 for i in range(100)]
   
   while True:
      bestsize = 0
      bestx = -1
      besty = -1
      
      for y in range(height-1, -1, -1):
         for x in range(width-1, -1, -1):
            if used[y][x]:
               continue
            
            bestcursize = 1
            start = grid[y][x]
            
            #x = 13
            #y = 0
            for testsize in range(2, 33):
               curV = start
               shouldBreak = False
               for ay in range(testsize):
                  for ax in range(testsize):
                     
                     cy = y+ay
                     cx = x+ax
                     
                     #if cy == y and cx == x:
                     #   continue
                     
                     if (not (0<=cy<height and 0<=cx<width)) or used[cy][cx]:
                        #print "out"
                        shouldBreak = True
                        break
                     
                     if curV != grid[cy][cx]:
                        shouldBreak = True
                        #print "invalid"
                        break
                     
                     curV = not curV
                  if testsize % 2 == 0:
                     curV = not curV
                     
                  if shouldBreak:
                     break
               if shouldBreak:
                  break
               
               bestcursize = testsize
            
            if bestcursize >= bestsize:
               bestsize = bestcursize
               bestx = x
               besty = y
            
      if bestsize == 0:
         break
      #print "remve %d at %d, %d" % (bestsize, bestx, besty)
      #break
      
      counts[bestsize] += 1
      
      for y in range(bestsize):
         for x in range(bestsize):
            used[besty+y][bestx+x] = True
   
   asd = 0
   for c in counts:
      if c != 0:
         asd += 1
   
   print "Case #%d: %d" % (caseNum+1, asd)
   
   for i, c in reversed(list(enumerate(counts))):
      if c != 0:
         print "%d %d" % (i, c)
   #print counts
   
   #print
   #break
         