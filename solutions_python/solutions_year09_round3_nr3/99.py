
def pb(prisonls,index,releseid):
    pos=prisonls[index].index(releseid)
    ahalf=prisonls[index][0:pos]
    bhalf=prisonls[index][pos+1:]
    prisonls.remove(prisonls[index])
    prisonls.append(ahalf)
    prisonls.append(bhalf)

def getminNum(P,Q,order):
    count=0
    prisonls=[range(1,P+1)]
    for x in xrange(0,Q):
        o=int(order[x])
        for i in xrange(0,len(prisonls)):
            if o not in prisonls[i]:continue
            else:
                count=count+len(prisonls[i])-1
                pb(prisonls,i,o)
        pass
    return count
    pass

if __name__=="__main__":
        
    filename='C-small-attempt0.in'
    infile=open('D:/My Documents/Downloads/gcj/'+filename,'r')
    outfile=open('D:/My Documents/Downloads/gcj/out.out','w')
    T=int( infile.readline())
    for x in xrange(0,T):
        PQ=infile.readline().replace('\n','').split(" ")
        P=int(PQ[0])
        Q=int(PQ[1])
        order=infile.readline().replace('\n','').split(" ")
        order.reverse()
        c=getminNum(P,Q,order)
        outfile.write("Case #"+str(x+1)+": "+str(c)+"\n")