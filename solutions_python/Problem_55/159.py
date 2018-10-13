import time
time.clock()

def ride(k,g,offset):
  money=0
  x = k
  riders =0
  while(x >= g[offset] and riders<len(g)):
    x -=g[offset]
    money+=g[offset]
    riders+=1
    offset+=1
    offset%=len(g)
  return [money,offset]

input = open("C-small-attempt2.in","r")
output = open("c.out", "w")
t = int(input.readline().strip())
for i in range(t):
  (r,k,n) = input.readline().split(" ")
  g = input.readline().split(" ")
  for j in range(len(g)):
    g[j] = int(g[j])
  money =0
  o=0
  for a in range(int(r)):
    (m,o)=ride(int(k),g,o)
    money+=m
  output.write ("Case #"+str(i+1)+": "+str(money)+"\n")
print(time.clock())
