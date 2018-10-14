def isallconsonants(s):
 return reduce(lambda x,y: x and y, [not(l in 'aeiou') for l in s])

def nvalue(name,n):
 subs=[]
 for i in range(len(name)-n+1):
  if isallconsonants(name[i:i+n]): subs.append((i,i+n))
 k=[0]*len(name)
 for s,e in subs:
  for n in range(s+1):
   k[n]=max(k[n],len(name)-e+1)
 return sum(k)

input = file('A-small-attempt0.in','rb+')
ncases = int(input.readline().strip())
out = file('A-small-attempt0.out','wb+')
for casen in range(ncases):
 s,n = input.readline().split(); n=int(n)
 out.write('Case #'+str(casen+1)+': '+str(nvalue(s,n))+'\r\n')