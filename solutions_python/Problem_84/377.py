cant = int(raw_input())
for t in range(cant):
  valor = raw_input().split(' ')
  r = int(valor[0])
  c = int(valor[1])
  mid = [] 
  ans = []
  nums = []
  for i in range(r):
    linea = raw_input()
    mid.append([])
    nums.append([])
    for j in range(c):
      mid[i].append(linea[j])
      nums[i].append(-1)
  
  imposible = False
  for i in range(r):
    if imposible:
      break
    for j in range(c):
      atras = 0 
      if j > 0:
        atras = nums[i][j-1]
      arriba = 0 
      if i > 0:
        arriba = nums[i-1][j] 
      
      if mid[i][j] == '.':
        nums[i][j] = 0
        if atras in [1,3] or arriba in [1,2]:
          imposible = True
          break
        continue
      
      if atras in [0,2,4] and arriba in [0,3,4] :
        nums[i][j] = 1 
        mid[i][j] = '/'
      elif atras == 1 and arriba in [0, 3, 4]:
        nums[i][j] = 2
        mid[i][j] = '\\' 
      elif atras in [0,2,4] and arriba == 1:
        mid[i][j] = '\\' 
        nums[i][j] = 3
      elif atras == 3 and arriba == 2:
        mid[i][j] = '/'
        nums[i][j] = 4
      else:
        imposible = True
        break
    if nums[i][c-1] in [1,3]:
      imposible = True
      break
  
  for j in range(c):
    if nums[r-1][j] in [1,2]:
      imposible = True
      break

  print "Case #{0}:".format(t+1)
  if imposible:
    print "Impossible"
  else:
    for i in range(r):
      print "".join(mid[i])
  
