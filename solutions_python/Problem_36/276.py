def t(l,w,x,y,occ):
  if y >= len(w): return occ
  a = 0
  while 1:
    a = l.find(w[y],x)
    x = a+1
    if a == -1:
      break
    if y==len(w)-1:
      occ += 1
    if x == len(l): break
    occ = t(l,w,x,y+1,occ)
  return occ
###

f = open("input.in","r")
g = open("input.out","w")
n = int(f.readline().rstrip("\n"))

word = "welcome to code jam"
for i in range(n):
  a = f.readline().rstrip("\n")
  b = t(a,word,0,0,0)
  b = b%10000
  l = 4-len(str(b))
  b = "0"*l+str(b)
  g.write("Case #"+str(i+1)+": "+b+"\n")
