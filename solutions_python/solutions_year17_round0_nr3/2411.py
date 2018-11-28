import sys
def f1():
  max=0
  id=0
  for i in xrange(len(a)-1):
    if (a[i+1]-a[i])>max:
        max=a[i+1]-a[i]
        id=i
  r=(a[id+1]-a[id])/2+a[id]
  a.append(r)
  a.sort()
  return r

sys.stdout = open('out.txt', 'w')
with open('a.in') as f:
    lines = f.readlines()
t=int(lines[0])
for p in xrange(t):
    n,k=(int(x)for x in lines[p+1].split())
    a=[0,n+1]
    for i in xrange(k):
        t=f1()
    i=a.index(t)
    q= a[i]-a[i-1]-1
    w= a[i+1]-a[i]-1
    if q>w:
        print "Case #"+str(p+1)+": "+str(q) +" "+str(w)
    else:
        print "Case #"+str(p+1)+": "+str(w) +" "+str(q)
