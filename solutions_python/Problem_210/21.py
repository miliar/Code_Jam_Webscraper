T = int(input())
for t in range(T):
  nc, nj = map(int, input().split())
  dc = [list(map(int, input().split())) for n in range(nc)]
  dj = [list(map(int, input().split())) for n in range(nj)]
  for v in dc: v.append(0)
  for v in dj: v.append(1)
  data = sorted(dc+dj)
  data.append(data[0][:])
  data[-1][0] += 1440
  data[-1][1] += 1440
  gaps = {(0,0): [], (0,1): 0, (1,0): 0, (1,1): []}
  total = {0:0, 1:0}
  res = 0
  for t1, t2 in zip(data, data[1:]):
    x = t1[2]
    y = t2[2]
    total[x] += t2[0] - t1[0]
    if x == y:
      gaps[(x,x)].append(t2[0] - t1[1]) 
    else:
      gaps[(x,y)] += t2[0] - t1[1]
      res += 1
      
  #print(data)    
  #print(total)    
  #print(gaps)    
  if total[0] > total[1]:
    delta = (total[0] - total[1]) // 2
    if delta > gaps[(0,1)]:
      delta -= gaps[(0,1)]
      for v in sorted(gaps[(0,0)], reverse = True):
        res += 2
        delta -= v
        if delta <= 0: break
  else:      
    delta = (total[1] - total[0]) // 2
    if delta > gaps[(1,0)]:
      delta -= gaps[(1,0)]
      for v in sorted(gaps[(1,1)], reverse = True):
        res += 2
        delta -= v
        if delta <= 0: break
  print("Case #"+str(t+1)+":", res)
  