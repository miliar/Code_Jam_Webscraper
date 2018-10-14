f = open('B-large.in', 'r')

T = int(f.readline().strip())



for t in xrange(T):

    N = int(f.readline().strip())
    dgs=str(N)

    num=0
    numl=[]
    if len(dgs)>1:
        for i in xrange(len(dgs)-1):

            if int(dgs[i]) <= int(dgs[i+1]):
                numl.append(dgs[i])
                if i+1==len(dgs)-1:
                    numl.append(dgs[i+1])
            else:
                numl.append(str(int(dgs[i])-1))
                j=len(numl)-1                
                while int(numl[j])<int(numl[j-1]):
                    numl[j]=str(9)
                    numl[j-1]=str(int(numl[j-1])-1)
                    j-=1
                    if j<=0:
                        break
                for x in xrange(i,len(dgs)-1):
                    numl.append(str(9))                
                    #print "x",x
                #print N,i
                break            
        num=int("".join(numl))
        #print len(str(int("".join(numl)))),len(dgs)
    else:
        num=N

    print 'Case #%d: %d'% (t+1,num)