#python 2.5
#ugliest piece of code ever
from string import join
a=file('B-large.in').read().split('\n');a.reverse()
cases=int(a.pop())
def fnext(place):
 x,y=place[1]
 ops3=[(x,y),(x,y-1),(x-1,y),(x+1,y),(x,y+1)];ops2=[];ops1=[]
 for l in ops3:
  if not(l[0]<0 or l[1]<0 or l[0]>=dims[1] or l[1]>=dims[0]):
   ops2.append(l)
 for l in ops2: ops1.append((arr[l[1]][l[0]],l))
 m=min(ops1)[0]
 for j in ops1:
  if j[0]==m: return j

def allof(x):
 m=0
 for l in x: m+=len(x[l])
 return m

def remove(x,y):
 c={}
 for l in x:
  if l!=y: c[l]=x[l]
 return c

out=file('B-large.out','w+')
for l in range(cases):
 dims=a.pop().split(' '); dims=[int(dims[0]),int(dims[1])]; arr=[]
 for m in range(dims[0]):
  k=a.pop().split()
  for i in range(len(k)): k[i]=int(k[i])
  arr.append(k)
 all=[]
 for y in range(dims[0]):
  for x in range(dims[1]):
   all.append((arr[y][x],(x,y)))
 all.sort();all.reverse();step={};basins={}
 for h in all: step[h]=fnext(h)
 for m in step:
  if step[m]==m: basins[m]=[m]; step=remove(step,m)
 while allof(basins)!=dims[0]*dims[1]:
  for x in basins:
   for m in step:
    if step[m] in basins[x]: basins[x].append(m); step=remove(step,m)
 order=[]
 for u in basins:
  cells=[]
  for m in basins[u]: cells.append(m[1][0]+m[1][1]*dims[1])
  order.append((min(cells),u))
 order.sort()
 alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 out1=[];alpha.reverse()
 for z in range(dims[0]): out1.append([0]*dims[1])
 for o in order:
  letter=alpha.pop()
  for j in basins[o[1]]: out1[j[1][1]][j[1][0]]=letter
 out.write('Case #'+str(l+1)+':\n')
 for y in out1: out.write(join(y,' ')+'\n')
 print l