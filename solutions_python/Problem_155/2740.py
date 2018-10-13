def solve(s):
  a=s.split(" ")
  f=0
  p=int(a[1][0])
  for i in range (1,int(a[0])+1):
    if i > p:
      d = i-p
      f = f + d
      p = p + d
    p = p + int(a[1][i])
  return f

fi = open("A-large.in","r")
fo = open("A-large.out","w")

n = int(fi.readline())

for i in range(1,n+1):
    fl = fi.readline()
    b = solve(fl)
    s=str(b)
    o= "Case #"+str(i)+": "+s
    fo.write(o+"\n")
    print(str(i))
fo.close()
fi.close()
print("fine")
