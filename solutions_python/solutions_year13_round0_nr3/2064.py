import math
f = open("c-small-attempt0.in","r")
out = open("output.txt","w")

count = int(f.readline())
      
nums = []
for i in range(1,1000):
  
  if i == 0:
    continue
  if str(i) == str(i)[::-1] and math.sqrt(i).is_integer():
    if str(int(math.sqrt(i))) == str(int(math.sqrt(i)))[::-1]:
      nums.append(i)


casecount = 1
for i in range(count):
  x = f.readline().strip().split(" ")
  minn = int(x[0])
  maxx = int(x[1])
  count = 0
  for j in nums:
    if j < minn:
      continue
    if j >= minn and j <= maxx:
      count +=1
    if j > maxx:
      break
  out.write("Case #" + str(casecount)+": " + str(count)+"\n")
  casecount +=1


f.close()
out.close()
