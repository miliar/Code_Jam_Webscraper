import sys

n = int(input())
for i in range(1, n+1):
  x = int(input())
  s1 = [sys.stdin.readline().strip() for _ in range(0, 4)]
  y = int(input())
  s2 = [sys.stdin.readline().strip() for _ in range(0, 4)]
  
  l1, l2 = s1[x-1].split(" "), s2[y-1].split(" ")
  common = list(set(l1) & set(l2))
  k = len(common)
  
  if k == 1:
    print "Case #%s: %s" % (i, common[0])
  elif k > 1:
    print "Case #%s: Bad magician!" % i
  else:
    print "Case #%s: Volunteer cheated!" % i
