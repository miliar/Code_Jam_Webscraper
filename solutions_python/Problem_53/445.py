s = open('A-large.in','r').read()
out = open('A-large.out','w')

new = s.split('\n')
#print new

n = 0
i = 0

pot = [1]
for k in range(1,31):
  pot.append(pot[k-1]*2)
#print pot

for s in new:
  if n == 0:
    n = int(s)
    continue
  
  s = s.split(' ')
  if len(s) < 2 :
    break
  
  i += 1
  N = int(s[0])
  K = int(s[1])
 # print N,K    
  
  p = pot[N]
  K -= p-1
  if K % p == 0:
    out.write("Case #" +str(i)+": ON\n")
  else: 
    out.write("Case #" +str(i)+": OFF\n")
  
  n = n-1
  print n
  if n == 0:
    break
