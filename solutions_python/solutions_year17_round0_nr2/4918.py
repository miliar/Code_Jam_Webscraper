fo=open("B-small-attempt0.in","r")
fw = open("output.out","w")
t=int(fo.readline())
for i in range(t):
   l=int(fo.readline())
   for p in range(l,0,-1):
      if list(str(p)) == list(sorted(str(p))):
         fw.write("Case #%d: %d\n" % (i+1, p))
         break
fo.close()
fw.close()
