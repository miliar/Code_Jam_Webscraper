import string
t=int(raw_input(''))

for i in xrange(1,t+1):
  a=string.split(raw_input(''))
  c=int(a[0])
  a=a[1:]
  cm={}
  for j in range(c):
    qq=a[j]
    cm[qq[0]+qq[1]]=qq[2]
    cm[qq[1]+qq[0]]=qq[2]
    
  a=a[c:]
  d=int(a[0])
  a=a[1:]
  op=[]
  for j in range(d):
    qq=a[j]
    op.append(qq[0]+qq[1])
    op.append(qq[1]+qq[0])
  a=a[d:]
  n=int(a[0])
  s=a[1]
  res=''
  
  for qq in s:
    res=res+qq
    if res[-2:] in cm:
      res=res[0:-2]+cm[res[-2:]]
    for j in res:
      if j+res[-1] in op:
         res=''
         break
        
  qq=''
  if len(res)>0:
    for j in res:
      qq=qq+j+', '
    qq='['+qq[0:-2]+']'
  else:
    qq='[]'
  print 'Case #'+str(i)+': '+qq
 

	
   
