fileo=open("B-small-attempt0.in","r")
h = 0
l = 0
file=open("output.txt","w")
t = fileo.readline()
p = int(t)
s = list(range(p))
for line in fileo:
 s[h]=line
 h += 1
for v in range(p):
 w = str(v + 1)
 f = int(s[v])
 n = f + 1
 for k in range(n):
  cp = 0
  if k <= 9:
   l = k
  else:
   st = str(k)
   u = list(st)
   ul = len(u)
   for o in range(ul):
    if o >= 1:
     j = ul - 1
     if int(u[o-1]) <= int(u[o]):
      cp += 1
      if cp == j:
       l = k
 lS = str(l)
 file.write("Case #" + w +": "+ lS)
 file.write("\n")
file.close()
