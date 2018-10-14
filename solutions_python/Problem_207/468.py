import io, os, sys

data = open(sys.argv[1]).readlines()
n = int(data[0])

print data
count = 0
i = 1
while count < n:
  count += 1
  print 'count', count
  A = data[i].split(" ")
  i += 1
  r = int(A[1])
  y = int(A[3])
  b = int(A[5])
  print A
  tmp = [r,y,b]
  tmp.sort()
  if tmp[2] > tmp[1] + tmp[0]:
    print 'Case #' + str(count) + ': IMPOSSIBLE'
    continue
  tmp.sort(reverse=True)
  print tmp
  name = ['', '', '']
  used = [False,False,False]
  color = [r,y,b]
  v = ['r','y','b']
  for j in range(3):
    for k in range(3):
      if used[k] == False and color[k] == tmp[j]:
        #print j,k
        used[k] = True
        name[j] = v[k]
        break
  print name
  ret = []
  a,b,c = tmp[0], tmp[1], tmp[2]
  for j in range(c):
    ret.append(name[0])
    ret.append(name[1])
    ret.append(name[2])
  for j in range(b-c):
    ret.append(name[0])
    ret.append(name[1])
  #for i in range(1,len(ret)):
  print ret, 'remaing', a-b
  num = 0
  boo = True
  while boo:
    if num == a-b:
      boo = False
      continue
    for j in range(1,len(ret)):
      if ret[j-1] != name[0] and ret[j] != name[0]:
        num += 1
        ret.insert(j, name[0])
        if num == a-b:
          boo = False
        break
  r = ''
  for j in ret:
    r += j
  print 'Case #' + str(count) + ': ' + r
    
  
