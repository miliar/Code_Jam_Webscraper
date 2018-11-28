f = open("i2")
t = int(f.readline())
for x in range(1,t+1):
  print "Case #"+str(x)+":",
  a,b,k = map(int, f.readline().split())
  z = 0
  for i in range(a):
    for j in range(b):
      if i&j<k:
        z+=1
  print z