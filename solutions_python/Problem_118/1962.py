from math import sqrt,ceil,floor

ip = open('C-small-attempt0.in', 'r')
op = open('output.txt', 'w')

t=int(ip.readline())
i=0;
while(i<t):
 i=i+1
 i_str=str(i)
 o='Case #{0}: '.format(i_str)
 op.write(o)
 line=ip.readline()
 AB=line.split()
 a=int(AB[0])
 b=int(AB[1])
 count=0
 for j in range(a,b+1):
  p=0
  q=0
  x=str(j)
  y=''.join(reversed(x))
  if x==y:
   p=1
  sq=sqrt(j)
  sq_c=ceil(sq)
  sq_f=floor(sq)
  if sq_c==sq_f:
   x=str(sq_c)
   y=''.join(reversed(x))
   if x==y:
    q=1
  if p==1 and q==1:
   count=count+1

 o='{0}\n'.format(str(count))
 op.write(o)

ip.close()
op.close()
