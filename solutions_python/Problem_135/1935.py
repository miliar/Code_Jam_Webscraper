
T = int(raw_input())

for c in xrange(T):
  r1 = int(raw_input())-1
  
  m1 = []
  
  for i in xrange(4):
    m1.append(map(int,raw_input().split()))

  m1 = m1[r1]

  r2 = int(raw_input())-1
  
  m2 = []
  
  for i in xrange(4):
    m2.append(map(int,raw_input().split()))

  m2 = m2[r2]

  a = []
  for i in m1:
    if i in m2:
      a.append(i)
  
  if(len(a) == 0):
    print 'Case #%d:'%(c+1),'Volunteer cheated!'
    
  if(len(a) > 1):
    print 'Case #%d:'%(c+1),'Bad magician!'
    
  if(len(a) == 1):
    print 'Case #%d:'%(c+1),a[0]
  


