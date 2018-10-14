import sys
t=input()
i=1
while i<=t:
  n1=input()-1
  l1=[] 
  s=sys.stdin.readline().strip().split()
  s=map(int,s)
  l1.append(s)
  s=sys.stdin.readline().strip().split()
  s=map(int,s)
  l1.append(s)
  s=sys.stdin.readline().strip().split()
  s=map(int,s)
  l1.append(s)
  s=sys.stdin.readline().strip().split()
  s=map(int,s)
  l1.append(s)
  n2=input()-1
  l2=[]
  s=sys.stdin.readline().strip().split()
  s=map(int,s)
  l2.append(s)
  s=sys.stdin.readline().strip().split()
  s=map(int,s)
  l2.append(s)
  s=sys.stdin.readline().strip().split()
  s=map(int,s)
  l2.append(s)
  s=sys.stdin.readline().strip().split()
  s=map(int,s)
  l2.append(s)
  #print l1,l2
  a=(l1[n1][0] in l2[n2] and l1[n1][1] not in l2[n2] and l1[n1][2] not in l2[n2] and l1[n1][3] not in l2[n2])
  b=(l1[n1][1] in l2[n2] and l1[n1][0] not in l2[n2] and l1[n1][2] not in l2[n2] and l1[n1][3] not in l2[n2])
  c=(l1[n1][2] in l2[n2] and l1[n1][0] not in l2[n2] and l1[n1][1] not in l2[n2] and l1[n1][3] not in l2[n2])
  d=(l1[n1][3] in l2[n2] and l1[n1][0] not in l2[n2] and l1[n1][1] not in l2[n2] and l1[n1][2] not in l2[n2])
  if  a or  b or  c or d:
       if a:
           print "Case #"+str(i)+":",l1[n1][0]
       if b:    
           print "Case #"+str(i)+":",l1[n1][1]
       if c:
           print "Case #"+str(i)+":",l1[n1][2]
       if d:
           print "Case #"+str(i)+":",l1[n1][3]
  elif l1[n1][0] in l2[n2] or l1[n1][1] in l2[n2] or l1[n1][2] in l2[n2] or l1[n1][3] in l2[n2]:
           print "Case #"+str(i)+":","Bad magician!"
  else:
           print "Case #"+str(i)+":","Volunteer cheated!" 
  i=i+1
