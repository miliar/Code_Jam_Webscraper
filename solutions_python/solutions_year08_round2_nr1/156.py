import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
   line = sys.stdin.readline().strip().split()
   n = int(line[0])
   A = int(line[1])
   B = int(line[2])
   C = int(line[3])
   D = int(line[4])
   x0 = int(line[5])
   y0 = int(line[6])
   M = int(line[7])

   X = x0
   Y = y0
   trees = []
   trees.append((X,Y))
   for j in range(1, n):
      X = (A * X + B) % M
      Y = (C * Y + D) % M
      trees.append((X,Y))

   answer = 0

   for j in range(0, len(trees)):
      for k in range(j+1, len(trees)):
         for l in range(k+1, len(trees)):
            cX = (trees[j][0] + trees[k][0] + trees[l][0])/3.0
            if float(int(cX)) != float(cX):
               continue
            cY = (trees[j][1] + trees[k][1] + trees[l][1])/3.0
            if float(int(cY)) != float(cY):
               continue
            answer += 1



   print "Case #%d: %d" %(i, answer)
      

