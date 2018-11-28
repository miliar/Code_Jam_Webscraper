f=open('C-small-attempt0.in')
noi=int(f.readline().rstrip('\r\n'))
i=1
ou=open('jam.out','w')
while i<=noi:
  re=f.readline()
  rs=re.split()
  a=int(rs[0])
  b=int(rs[1])
  c=[]
  ans=0
  for x in range(a,b+1):
      c.append(x)
  for ind,x in enumerate(c):
      for y in c[ind+1:]:
          n=str(x)
          m=str(y)
          if len(n)==len(m) and len(n)>1 and len(m)>1:
             ki=1 
             while ki <len(n):
                 temp=n[-1:-(ki)-1:-1][::-1]+n[:-(ki)]
                 if temp[0]!='0':
                  if temp==m:
                     ans+=1
                     break
                 ki+=1   
          else :
              break
          
      
      
  print("Case #%s:"%(i),ans,file=ou)
  i+=1
ou.close()
f.close()
