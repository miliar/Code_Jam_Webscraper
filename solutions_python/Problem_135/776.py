import sys

if len(sys.argv)<2:
  exit()

fname = sys.argv[1]
f = open(fname, "r")
n = int(f.readline())

for i in range(0, n):
  r1 = int(f.readline())-1
  m1 = []
  for j in range(0, 4):
    m1.append([int(x) for x in f.readline().split()])
    
  r2 = int(f.readline())-1
  m2 = []
  for j in range(0, 4):
    m2.append([int(x) for x in f.readline().split()])
    
  r = []
  for c in m1[r1]:
    if c in m2[r2]:
      r.append(c)
  if len(r) == 1:
    print "Case #%d: %d" % (i+1, r[0])
  elif len(r) > 1:
    print "Case #%d: Bad magician!" % (i+1)
  else:
    print "Case #%d: Volunteer cheated!" % (i+1)

  

f.close()

