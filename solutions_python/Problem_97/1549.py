def recycled(a,b):
    if len(str(a))!=len(str(b)):
        return 0
    final = str(a) + str(a);
    if final.find(str(b))!=-1:
        return 1
    return 0

n=input()
iterator=1
while n!=0:
    count=0
    s=raw_input()
    a=int(s.split(' ')[0])
    b=int(s.split(' ')[1])
    for i in xrange(a,b+1):
        for j in xrange(i+1,b+1):
            if recycled(i,j):
                count+=1
    print 'Case #'+str(iterator)+": "+str(count)
    n=n-1
    iterator+=1
