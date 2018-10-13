# rynkruger@gmail.com

def rotate(l):
  a = l[0]
  del l[0]
  l.append(a)
  return a

cases = int(raw_input())
for case in range(1,cases+1):
  inp = raw_input().split(" ")
  r = int(inp[0])
  k = int(inp[1])
  n = int(inp[2])
  l = []
  groups = raw_input().split(" ")
  for i in groups:
    l.append(int(i))
  sum = 0
  for i in range(0,r):
    cur = 0
    j = 0
    while cur+l[0] <=k and j < n:
      cur+= rotate(l)
      j+=1
    sum+=cur
  print "Case #%d: %d"%(case,sum)

