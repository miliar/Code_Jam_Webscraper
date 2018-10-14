
#some convinient function

def make_primelist(size):
  global prime
  from math import sqrt
  _prime=[1 for i in xrange(size+1)]
  _prime[0]=0
  _prime[1]=0
  for i in xrange(size):
    if i*i>size:
      break
    if _prime[i]==0:
      continue
    for k in xrange(2*i,size+1,i):
      _prime[k]=0
  prime=_prime

choice_max=2000
dp_choice=[[None for i in xrange(choice_max+1)] for j in xrange(choice_max+1)]
def choice(n,m): #return (n+m)!/(n!m!)
  if n<0 or m<0:
    return 0
  if dp_choice[n][m]!=None:
    return dp_choice[n][m]
  if n==m==0:
    ret=1
  else:
    ret=choice(n-1,m)+choice(n,m-1)
  dp_choice[n][m]=ret
  return ret

def inverse(x,M): #1/x mod m
  x=x%M
  if x==0 or M<=0:
    raise
  a,b,c,d=1,0,0,1
  v1,v2=x,M
  while v2:
    n=v1/v2
    v1,v2=v2,v1-n*v2
    a, b, c, d = c, d, a-n*c, b-n*d
  if v1!=1:
    raise
  return a%M

def div(a,b,M):
  return a*inverse(b,M)%M

def gcd(x,y):
  while y:
    x,y=y,x%y
  return x

"""
example
choice(0,5)==1 and choice(1,4)==5 and choice(2,3)==10
make_primelist(6); prime==[0,0,1,1,0,1,0]
inverse(3,10) == 7
div(7,9,10) == 3  because 27/9==3
gcd(10,15) == 5
"""



def readints():
  return map(int,raw_input().split())

def main():
  for T in xrange(input()):
    N,pd,pg=readints()
    m=min(200,N)
    s="Broken"
    for i in xrange(1,m+1):
      if (pg==0 or pg==100) and pd!=pg:break
      if pd*i%100==0:
        s="Possible"
        break
    print "Case #%s: %s"%(T+1,s)
  pass



if __name__=='__main__':
  main()



