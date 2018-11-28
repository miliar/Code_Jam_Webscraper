import sys
wt=sys.stdout.write

def test(a,b):
    a=str(a)
    b=str(b)
    if len(a)!=len(b):return False
    for n in xrange(1,len(a)+1):
        if a[n:]+a[0:n]==b:
            return True
    return False

f=open('a3.in')
NUM=int(f.readline())
for n in xrange(1,NUM+1):
    wt('Case #%d: '%n)
    l=map(int,f.readline().split(' '))
    sum=0
    for a in xrange(l[0],l[1]):
        for b in xrange(a+1,l[1]+1):
            if test(a,b):
                sum+=1
    print sum

