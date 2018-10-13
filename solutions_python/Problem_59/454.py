f=open("/tmp/A-large.in",'r')
o=open("out.txt",'w')

T = int(f.readline())

for p in range(T):
  
  fa = {}
  x = f.readline().split()
  
  N , M = int(x[0]) , int (x[1])
  count = 0
  for i in range(N):
    s = f.readline()
    s = s[:len(s) - 1]
    path = s.split('/')
    path[0] = '/'
    l =  len(path)  
    for j in range(l-1):
      fa[tuple(path[:l - j])] = tuple(path[ : l - j - 1 ])
      
  for i in range(M):
    s = f.readline()
    s = s[:len(s) - 1]
    path = s.split('/')
    path[0] = '/'
    l = len(path)
    
    for j in range(1,l):
      x = tuple(path[:j+1])
      if not x in fa.keys():
        break
    if tuple(path[:j+1]) in fa.keys():
      continue
    while j < l :
      j += 1
      fa[tuple(path[:j])] = tuple(path[:j-1])
      count += 1
    
  o.write("Case #%d: %d\n" %(p+1,count))
  
