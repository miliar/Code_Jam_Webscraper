import time
time.clock()

def g(a,b):
  while b!=0:
    x = a%b
    a = b
    b = x
  return a

def apox(x,y):
  flag =1
  gcf = 1
  for i in range(x-1):
    if(flag):
      gcf = y[i+1]-y[i]
      flag = 0
    else:
      gcf = g(gcf,y[i+1]-y[i])
  z = gcf - y[0]%gcf
  z %= gcf
  return z

input = open("B-large.in","r")
output = open("b.out", "w")
c = int(input.readline().strip())
for i in range(c):
  (n,t) = input.readline().strip().split(" ",1)
  #print(k)
  t = t.split(" ")
  for j in range(len(t)):
    t[j] = int(t[j])
  t.sort()
  print(t)
  output.write ("Case #"+str(i+1)+": "+str(apox(int(n),t))+"\n")
print(time.clock())
