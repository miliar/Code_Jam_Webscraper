r=open('A-large.in')
tem=r.readline()
l,d,n=map(int,tem.split())
temp=r.readlines()
aa=temp[:d]
bb=temp[d:]
ll=[]
for i in bb:
 s=i.split('(')
 for j in s:
  if ')' in j:
    kk=j.split(')')
    if len(kk)>1:
      ll.append(kk[0])
      ll.extend(list(kk[1]))
    else:
      ll.extend(kk)
  else:
    ll.extend(list(j))

mm=[]
for i in ll:
 if i :
  if i!='\n':
   mm.append(i)


sss=''
m=0
for i in range(n):
 tem=0
 n=0
 for j in range(d):
  for k in range(l):
   f=1
   if aa[j][k] not in mm[m+k]:
    f=0
    break
  if f==1:
    tem+=1
 m+=l
 sss+= 'Case #%d: %d\r\n' % (i+1,tem)
   
print sss 
w=open('out.txt','w')
w.write(sss)
w.close()
