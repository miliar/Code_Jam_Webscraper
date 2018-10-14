
t=int(raw_input())
for i in xrange(1, t+1):
    n= int(raw_input())
    nn=n
    l=[]
    while n >0:
        l = [n %10]+l
        n=n/10
    br=-1
    for j in xrange(1, len(l)):
        if l[j-1] > l[j]:
            br=j-1
            break
#    print br
    if br < 0:
        ans =nn
    else:
        while br >0 and l[br]==l[br-1]:
            br -=1
        l[br] -=1
        for k in xrange(br+1, len(l)):
            l[k]=9
        ans=0
        for k2 in xrange(len(l)):
            ans = l[k2] + 10*ans
 
    print "Case #%d: %d" % (i, ans)
 