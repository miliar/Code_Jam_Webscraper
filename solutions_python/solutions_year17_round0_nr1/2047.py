def test(s,n):
 res = 0
 t = list(s)
 for i in range(len(s)-n+1):
  if t[i] == '-':
   res += 1
   for j in range(n):
    if t[i+j] == '-':
     t[i+j] = '+';
    else:
     t[i+j] = '-';
 if any(r=='-' for r in t):
  return "IMPOSSIBLE"
 else:
  return str(res)

with open("A-large.in","r") as f:
 inp = [l.strip('\n') for l in f.readlines()]

f = open("A-large.out","w")
for i in range(int(inp[0])):
 j = i+1
 data = inp[j].split(' ')
 result = test(data[0],int(data[1]))
 f.write("Case #" + str(j) + ": " + result + "\n")

f.close()
