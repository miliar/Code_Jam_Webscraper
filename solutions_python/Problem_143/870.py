import sys
f=open(sys.argv[1])
o=open(sys.argv[2],'a')
cases=int(f.readline())
case=0
count=0
while cases:
    a,b,c=f.readline().split()
    a=int(a)
    b=int(b)
    c=int(c)
    for i in xrange(a):
        for j in xrange(b):
            if(i&j<c):
                count+=1
    cases-=1
    case+=1
    o.write('Case #%d: %d\n' %(case,count))
    count=0
    
