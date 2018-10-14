t = int(raw_input())
for i in range(0, t):
  s = raw_input()
  d = s.split(" ")
  d[0] = int(d[0])
  d[1] = int(d[1])
  d[2] = int(d[2])
  s = raw_input()
  g = s.split(" ")
  pos = 0
  res = 0
  r = [[-1 for x in range(2)] for y in range(d[2]+1)]
  #r[0] = [0, 0]
  for j in range(1, d[0]+1):
    tmp = 0
    index = -1
    for k in range(0, d[2]):
      tmp += int(g[(pos+k)%d[2]])
      if tmp > d[1]:
        tmp -= int(g[(pos+k)%d[2]])
        break
      index = (pos+k)%d[2]
    res += tmp
    pos = (index + 1)% d[2]
#    print pos, index, tmp, res
    if r[index][0] != -1:
#      print j,index,r[index][0]
#      print res
      dis = j - r[index][0]
      t = res - r[index][1]
      res += int((d[0] - j) / dis) * t
      j += int((d[0] - j) / dis)* dis
      break
    r[index][1] = res
    r[index][0] = j
  for m in range(j, d[0]):
    tmp = 0
    index = -1
    for k in range(0, d[2]):
      tmp += int(g[(pos+k)%d[2]])
      if tmp > d[1]:
        tmp -= int(g[(pos+k)%d[2]])
        break
      index = (pos+k)%d[2]
    res += tmp
    pos = (index + 1)% d[2]
  print "Case #%d: %s" % (i+1, str(res))
