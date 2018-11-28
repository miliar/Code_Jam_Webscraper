#!/usr/bin/python3
import fileinput

f=fileinput.input()
T=int(f.readline())

table={
( '-1' , '-1' ) : '1',
( '-1' , '-i' ) : 'i',
( '-1' , '-j' ) : 'j',
( '-1' , '-k' ) : 'k',
( '-1' , '1' ) : '-1',
( '-1' , 'i' ) : '-i',
( '-1' , 'j' ) : '-j',
( '-1' , 'k' ) : '-k',
( '-i' , '-1' ) : 'i',
( '-i' , '-i' ) : '-1',
( '-i' , '-j' ) : 'k',
( '-i' , '-k' ) : '-j',
( '-i' , '1' ) : '-i',
( '-i' , 'i' ) : '1',
( '-i' , 'j' ) : '-k',
( '-i' , 'k' ) : 'j',
( '-j' , '-1' ) : 'j',
( '-j' , '-i' ) : '-k',
( '-j' , '-j' ) : '-1',
( '-j' , '-k' ) : 'i',
( '-j' , '1' ) : '-j',
( '-j' , 'i' ) : 'k',
( '-j' , 'j' ) : '1',
( '-j' , 'k' ) : '-i',
( '-k' , '-1' ) : 'k',
( '-k' , '-i' ) : 'j',
( '-k' , '-j' ) : '-i',
( '-k' , '-k' ) : '-1',
( '-k' , '1' ) : '-k',
( '-k' , 'i' ) : '-j',
( '-k' , 'j' ) : 'i',
( '-k' , 'k' ) : '1',
( '1' , '-1' ) : '-1',
( '1' , '-i' ) : '-i',
( '1' , '-j' ) : '-j',
( '1' , '-k' ) : '-k',
( '1' , '1' ) : '1',
( '1' , 'i' ) : 'i',
( '1' , 'j' ) : 'j',
( '1' , 'k' ) : 'k',
( 'i' , '-1' ) : '-i',
( 'i' , '-i' ) : '1',
( 'i' , '-j' ) : '-k',
( 'i' , '-k' ) : 'j',
( 'i' , '1' ) : 'i',
( 'i' , 'i' ) : '-1',
( 'i' , 'j' ) : 'k',
( 'i' , 'k' ) : '-j',
( 'j' , '-1' ) : '-j',
( 'j' , '-i' ) : 'k',
( 'j' , '-j' ) : '1',
( 'j' , '-k' ) : '-i',
( 'j' , '1' ) : 'j',
( 'j' , 'i' ) : '-k',
( 'j' , 'j' ) : '-1',
( 'j' , 'k' ) : 'i',
( 'k' , '-1' ) : '-k',
( 'k' , '-i' ) : '-j',
( 'k' , '-j' ) : 'i',
( 'k' , '-k' ) : '1',
( 'k' , '1' ) : 'k',
( 'k' , 'i' ) : 'j',
( 'k' , 'j' ) : '-i',
( 'k' , 'k' ) : '-1'
}


def mul(a,b):
  c=(a,b)
  return table[c]

  
def qpow(a,n):
 sgn=1
 if len(a)>1:
  sgn=-1 
 if a in ('1','-1'):
   return str(int(a)**n)
 a=a[-1]
 sgn=(sgn**n)*(-1)**(n//2)
 if n%2==0:
    return str(sgn)
 elif sgn==-1:
    return '-'+a
 else:
    return a


for case in range(T):

  L,X=map(int,f.readline().split())
  ijk=f.readline().strip()
  setlen=len(set(ijk))
  p="1"
  out="NO"
  for e in ijk:
   p=mul(p,e)
  pwr=qpow(p,X)
  if pwr=='-1':
   if p=='-1':
    if setlen>2 or X>1:
     out="YES"
   elif setlen>1 and X>2:
     out="YES"   
   elif setlen>2 and X>1:
     out="YES"
  print("Case #"+str(case+1)+":",out)

     