def findBest(currentTick, timeTaken) :
      if (X/currentTick) > ((C/currentTick) + (X/(currentTick + F))) :
            return findBest(currentTick + F, timeTaken + (C/currentTick))
      else :
            return timeTaken +(X/currentTick)


fin = open('B-large.in', 'r')
fout = open('output.txt', 'w')
T = eval(fin.readline())
C,F,X = 0.0 , 0.0, 0.0
t, i, j = 0, 0, 0
while t in range(0, T) :
      C, F, X = fin.readline().split(' ')
      C = float(C)
      F = float(F)
      X = float(X)
      currentTick = 2.0
      timeTaken = 0
      while (X/currentTick) > ((C/currentTick) + (X/(currentTick + F))) :
            #print((X/currentTick), ((C/currentTick) + (X/(currentTick + F)) ))
            timeTaken = timeTaken + (C/currentTick)
            currentTick = currentTick + F
      totalSecs = timeTaken + (X/currentTick)
      #totalSecs = findBest(currentTick, 0)
      
      fout.write("Case #"+str(t+1)+": " + str("%.7f"%round(totalSecs,7))+"\n")
      #print(t)
      t = t + 1
fout.close()
fin.close()
