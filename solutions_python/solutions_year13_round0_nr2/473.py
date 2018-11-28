import fileinput
fi = fileinput.input()

T = int(fi.readline())

for case in xrange(T):
   N,M = map(int, fi.readline().strip().split())
   field = []
   fieldStat = []
   for line in xrange(N):
      field.append(map(int, fi.readline().strip().split()))
      fieldStat.append(field[-1][:])
   #print field
   for row in xrange(N):
      rowMax = max(field[row])
      for col in xrange(M):
          if field[row][col] == rowMax: fieldStat[row][col] = 0
   for col in xrange(M):
      colMax = max([field[row][col] for row in xrange(N)])
      for row in xrange(N):
          if field[row][col] == colMax: fieldStat[row][col] = 0
   
   #print fieldStat
   possible = 'YES'
   for row in xrange(N):
      for col in xrange(M):
         if fieldStat[row][col]!=0:
             possible = 'NO'
   print 'Case #'+str(case+1)+': '+possible
