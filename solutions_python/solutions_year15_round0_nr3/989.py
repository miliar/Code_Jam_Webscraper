class quat:
 def __init__(self,r,i,j,k):
  self.r=r; self.i=i; self.j=j; self.k=k
 def __mul__(self,other):
  a1,b1,c1,d1=self.r,self.i,self.j,self.k
  a2,b2,c2,d2=other.r,other.i,other.j,other.k
  return quat(a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+a2*b1+c1*d2-d1*c2, a1*c2-b1*d2+a2*c1+d1*b2, a1*d2+b1*c2-c1*b2+a2*d1)
 def __repr__(self):
  u=[self.r,self.i,self.j,self.k]; v=filter(lambda n: u[n]!=0, [0,1,2,3])
  if len(v)==1 and abs(u[v[0]])==1: return (str(u[v[0]])+['','i','j','k'][v[0]]).replace('1','')
  else: return '%+i%+ii%+ij%+ik'%(self.r,self.i,self.j,self.k)

# print quat(0,0,1,0)*quat(0,1,0,0)

unitquats={'i':quat(0,1,0,0), 'j':quat(0,0,1,0), 'k':quat(0,0,0,1)}
def simplify(s):
 out=quat(1,0,0,0)
 for l in s: out=out*unitquats[l]
 return out

#print str(simplify('ijk'*1000))

def solve(s,n):
 t=str(simplify(s))
 if t=='1': return False
 elif t=='-':
  if n%2==0: return False
 elif n%4!=2: return False
 u=s*min(n,12)
 out=quat(1,0,0,0); c=0
 while str(out)!='i' and c<len(u): out*=unitquats[u[c]]; c+=1
 if  str(out)=='i':
  out=quat(1,0,0,0)
  while str(out)!='j' and c<len(u): out*=unitquats[u[c]]; c+=1
  if str(out)=='j':
   return True
  else: return False
 else: return False
 

inp=file('C-small-attempt1.in','rb+'); outp=file('C-small-attempt1.out','wb+')
for casen in range(1,int(inp.readline().strip())+1):
 l,x=inp.readline().strip().split()
 s=inp.readline().strip()
 sol=solve(s,int(x))
 #print s,x,sol
 print 'Case #%i: '%casen+['NO','YES'][sol]
 outp.write('Case #%i: '%casen+['NO','YES'][sol]+'\r\n')