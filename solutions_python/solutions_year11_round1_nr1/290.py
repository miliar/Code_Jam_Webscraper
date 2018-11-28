f = 'a.txt'
r = open(f,'r')
t = int(r.readline())

w = open('out.txt','w')
k = 0
while k< t:
  n = r.readline()
  a,b,c = map(int,n.strip().split())
  flag = False
  for i in range(1,a+1):
    for j in range(1,101):
       if (i*b/100.0 - int(i*b/100.0) > 0.001):
         continue
       if (j*c/100.0 - int(j*c/100.0) > 0.001):
         continue
       if i*b <= c*j and j>=i and j*(100-c)>=i*(100-b):
         flag = True
         break
    if flag:
      break

  if flag:
    xx = 'Case #%d: Possible\n' % (k+1) 
  else:
    xx = 'Case #%d: Broken\n' % (k+1)
  w.write(xx)  
  k+=1

w.close()
r.close()
  
  