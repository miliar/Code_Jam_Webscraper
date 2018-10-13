from time import time

inp = open('b.in', 'r+')
out = open('b.out', 'w')

T = int(inp.readline())

for t in range(T):
  s = inp.readline().strip()
  o=[]
  lastChange = 0 
  good = True
  for i in range(len(s)):
    if i == 0:
      continue

    if int(s[i]) < int(s[i-1]):
      good = False
      break

    if s[i] != s[i-1]:
      lastChange = i

  if good:
    o = s
  else:
    if lastChange > 0 or s[0] != "1":
      o = s[:lastChange] + str(int(s[lastChange]) - 1) + "9"*(len(s) - lastChange - 1)
    else:
      o = "9"*(len(s) - 1)

  
  out.write("Case #"+str(t+1)+": "+o+"\n")

out.close()