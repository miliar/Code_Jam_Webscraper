import time
time.clock()

def cross(x1,y1,x2,y2):
  if x1>x2:
    return y1<y2
  return y1>y2
  
input = open("A-large.in","r")
output = open("a.out", "w")
t = int(input.readline().strip())
for i in range(t):
  n = int(input.readline().strip())
  lines = []
  count = 0
  for j in range(n):
    (a,b) = input.readline().strip().split(" ")
    a=int(a)
    b=int(b)
    for l in range(len(lines)):
      (c,d)=lines[l]
      if cross(a,b,c,d):
        count+=1
    lines.append([a,b])
  output.write ("Case #"+str(i+1)+": "+str(count)+"\n")
print(time.clock())
