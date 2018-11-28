n1=1111


f1=open("in")
f2=open('out','w')

loop=int(f1.readline())

for ii in range(1,loop+1):
    count=0
    ss=f1.readline().split()
    n1=int(ss[0])
    n2=int(ss[1])
    done = []
    for i in range(int(n1),int(n2)+1):
        for k in range(1,len(str(i))):
            s1=str(i)
            st=s1[k:]+s1[:k]
            #print st
            if int(s1) < int(st) and int(st) >= n1 and int(st) <= n2 and [s1,st] not in done:
                print st,s1
                print "done : ", done
                done.append([s1,st])
                count = count + 1
                #print "here"
            #if int(st) >= n1 and int(st) <= n2:
    print count
    toprint = "Case #"+str(ii)+': '+str(count)+'\n'
    f2.write(toprint)
    #print int("0101")