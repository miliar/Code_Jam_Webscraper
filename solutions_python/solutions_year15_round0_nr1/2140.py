with open('/home/gauravjs/Documents/Google Code Jam/2015Q/input-a-large','r') as f:
    cases=int(f.readline())
    lines=f.readlines()
inputs=[]
#print 'cases:',cases
#print 'lines:',lines
for i in range(cases):
  x=0
  added=0
  n,s=lines[i].split(' ')
  for j in range(int(n)+1):
    if j>x:
      a=j-x
      added+=a
      x+=a
    x+=int(s[j])
  print "Case #" + str(i+1) + ": " + str(added)
