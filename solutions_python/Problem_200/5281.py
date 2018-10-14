f=open("B-small-attempt7.in","r")
p=open("small-attempt7.in","w")
nm=f.readline()
i=1
while i<=int(nm):
      s=f.readline()#.strip()
      #print(s)
      j=int(s)

      if j<10:
          p.write('Case #%d: %d\n'%(i,j))

      else:
          while j>9:#//numbers less than it
                  a=list(str(j))
                  #print(s)
                  ll=0
                  k=0
                  while k<len(a)-1:
                      if(int(a[k])-int(a[k+1]) >0):
                          ll=1
                          break
                      k+=1
                  if ll==0:
                      p.write('Case #%d: %d\n'%(i,j))
                      break
                  j-=1

      i+=1
f.close()
p.close()
