
import math
a=open("in.txt","r")
b=a.read()
b=b.split()
print b
w=open("out","w")
i=1
for i in range(len(b)):
    b[i]=int(b[i])
i=1
z=1
while 1:
  ans=0
  ct=b[i]
  s=b[i+1]
  p=b[i+2]
  for k in range(ct):
    t=b[i+3+k]
    t-=p
    if t<0:
      continue
    f=math.floor(t/2)
    if f<p:
                    if p-f<2 and p-f>=0:
                        ans+=1
                    elif p-f==2:
                        if s>0:
                            s-=1
                            ans+=1
                        else:
                            continue
                    else:
                        continue
    else:
          ans+=1
  l="Case #"+str(z)+": "+str(ans)+"\n"
  z+=1
  w.write(l)
  i=i+3+ct
  if i>=len(b):break
w.close()
a.close() 
