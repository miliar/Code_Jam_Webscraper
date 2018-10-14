#import psyco
#psyco.full()
import pdb

def getint():
  return int(f.readline().strip())

def getstr():
  return f.readline().strip()

def getarr():
  s=f.readline().strip().split()
  for i in range(len(s)):
    s[i]=int(s[i])
  return s

def getwords():
  return f.readline().strip().split()

def getnode():
  tmp=getstr()
  #pdb.set_trace()
  while tmp.split()[0]==')':
    tmp=getstr()
  tmp=tmp[1:]
  if ')' in tmp:
    if tmp[len(tmp)-2]==')':
      return [float(tmp[:len(tmp)-2])]
    return [float(tmp[:len(tmp)-1])]
  else:
    node=tmp.split()
    node[0]=float(node[0])
    node.append(getnode())
    node.append(getnode())
    return node

def dotree(node):
  global p, char
  p=p*node[0]
  if len(node)>1:
    if node[1] in char:
      dotree(node[2])
    else:
      dotree(node[3])

def getanimal():
  tmp=getstr().split()
  global char
  char=tmp[2:]
  dotree(tree)
    

f=open('A-large.in','r')
fo=open('A-large.out','w')

ncases=getint()

for i in range(ncases):
  L=getint()
  j=0
  tree=getnode()
  A=getstr()
  while A.split()[0]==')':
    A=getstr()
  A=int(A)
  fo.write('Case #%d:\n'%(i+1))
  for j in range(A):
    global p
    p =1
    getanimal()
    fo.write('%0.7f\n'%(p))
  
  
f.close()
fo.close()
    
    
