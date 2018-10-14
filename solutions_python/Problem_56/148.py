t = int(raw_input())
for curCase in range(t):
   n, k = map(int, raw_input().split())
   g = [[0 for j in range(n)] for i in range(n)]
   ng = [[0 for j in range(n)] for i in range(n)]
   lasts = [n-1 for i in range(n)]
   for y in range(n):
      for x, c in enumerate(raw_input()):
         if c == 'R' or c == 'B':
            lasts[y] = x
         if c == 'R':
            g[y][x] = 1
         elif c == 'B':
            g[y][x] = 2
   
   for y in range(n):
      for x in range(n):
         ng[y][x] = g[(n-1-x)][y]
   
   for x in range(n):
      cur = 0
      for y in range(n-1, -1, -1):
         if ng[y][x] == 0:
            cur += 1
         else:
            ng[y+cur][x] = ng[y][x]
      for y in range(cur):
         ng[y][x] = 0
   
   
   won = [False, False]
   dx = [-1, -1, 0, 1, 1, 1, 0, -1]
   dy = [0, -1, -1, -1, 0, 1, 1, 1]
   for y in range(n):
      for x in range(n):
         
         cur = ng[y][x]
         if cur == 0:
            continue
         if won[cur-1]:
            continue
         
         for dn in range(8):
            found = True
            for cnt in range(k):
               nx = x+cnt*dx[dn]
               ny = y+cnt*dy[dn]
               if nx < 0 or nx >= n or ny < 0 or ny >= n:
                  found = False
                  break
               if ng[ny][nx] != cur:
                  found = False
                  break
            
            if found:
               won[cur-1] = True
               break
   
   if not any(won):
      winner = "Neither"
   elif all(won):
      winner = "Both"
   elif won[0]:
      winner = "Red"
   elif won[1]:
      winner = "Blue"
   
   print "Case #%d: %s" % (curCase+1, winner)