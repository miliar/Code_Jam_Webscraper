import string

def gcd(a, b):
  if b==0:
    return a
  else:
    return gcd(b, a%b)


f = open("B-large.in", "r")
n = int(f.readline())
for i in range (1, n+1):
 s = f.readline();
 print "Case #%d:" % (i),
 a=[]
 b=""
 for j in s:
  if j==" " or j=="\n":
    if len(b)==0:
      continue;
    else:
      a.append(long(b));
      b=""
  else:
    b=b+j;
 del a[0]
 c = [i-a[0] for i in a]
 del c[0]
 d = c[0];
 if d<0: d=-d
 for i in range(1, len(c)):
   if c[i]<0: c[i]=-c[i]
   d = gcd(d, c[i])
 e=a[0]%d;
 e=d-e;
 if e==d: e=0
 print e
 
 
f.close
