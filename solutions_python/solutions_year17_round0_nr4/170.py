def solve():
    f=open("D-small-attempt1.in")
    f2=open("output.txt",'w')
    lines=f.readlines()
    t=int(lines[0])
    current=1
    # t=input()
    for test in xrange(1,t+1):
        n,m=map(int,lines[current].split())
        current+=1
        # n,m=map(int,raw_input().split())
        d,count,terminal={},0,0
        for x in xrange(m):
            # model,i,j=raw_input().split()
            model,i,j=lines[current].split()
            current+=1
            d[(int(i),int(j))]=model
            if model=='x' or model=='o':
                if model!='o':
                    count+=1
                terminal=int(j)

        ans,req=3*n-2,count+n-m+2*n-3
        if n==1:ans,req=2,count+n-m
        if not terminal:
            count=1
            terminal=1
            if (1,1) in d:
                req+=1
            d[(1,1)]='o'

        # print "Case #{}: {} {}\n".format(test,ans,req)
        f2.write("Case #{}: {} {}\n".format(test,ans,req))
        if count:
            # print 'o {} {}\n'.format(1,terminal)
            f2.write('o {} {}\n'.format(1,terminal))

        for x in xrange(1,n+1):
            if not((1,x) in d):
                # print '+',1,x
                f2.write('+ {} {}\n'.format(1,x))
        # print terminal,n
        if terminal!=n:
            y,add=1,1
        else:
            y,add=n-1,-1
        # print y,add
        for x in xrange(2,n+1):
            if y==terminal:y+=add
            f2.write('x {} {}\n'.format(x,y))
            # print 'x {} {}\n'.format(x,y)
            y+=add

        for x in xrange(2,n):
            # print "+",n,x
            f2.write('+ {} {}\n'.format(n,x))

    f2.close()
    f.close()
solve()
