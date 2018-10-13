def solve():
    f=open("A-large.in")
    f2=open("output.txt",'w')
    lines=f.readlines()
    t=int(lines[0])
    current=1
    # t=input()
    for test in xrange(1,t+1):
        d,n=map(int,lines[current].split())
        current+=1
        # d,n=map(int,raw_input().split())
        time=[]
        for x in xrange(n):
             ki,si=map(int,lines[current].split())
            #  ki,si=map(int,raw_input().split())
             time.append(((d-ki)*1.0)/si)
             current+=1
        ans=d/max(time)
        # print "%.7f"%ans
        f2.write("Case #{}: {}\n".format(test,"%.7f"%ans))
    f2.close()
    f.close()
solve()
