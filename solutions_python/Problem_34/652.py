kws=set()
def fenjie(s):
    rs=[]
    s=s.replace("\n","")
    ls=list(s)
    while len(ls)>0:
        if ls[0]!='(':
            rs.append(ls[0])
            ls=ls[1:]
        else:
            g=ls.index(')')
            rs.append(ls[1:g])
            ls=ls[g+1:]
    return rs

def getresult(ls,index,value,L,c):
    if(len(ls)!=L):
        return
    if index==L-1:
        for t in ls[index]:
            if value+t in kws:
                c['count']=c['count']+1
    else:
        for t in ls[index]:
            if value+t in kws:
                 getresult(ls,index+1,value+t,L,c)
            

if __name__=='__main__':
    infile=open('D:/My Documents/Downloads/A-small-attempt0.in','r')
    outfile=open('D:/My Documents/Downloads/A.out','w')
    LDN=infile.readline().replace('\n','').split(' ')
    L=int(LDN[0])
    D=int(LDN[1])
    N=int(LDN[2])
    for i in xrange(D):
        kw=infile.readline().replace('\n','')
        for n in xrange(L):
            kws.add(''.join(kw[0:n+1]))
    print kws,len(kws)
    cout=0;
    for x in infile:
        c={}
        cout=cout+1
        wl=fenjie(x)
        c['count']=0
        getresult(wl,0,'',L,c)
        print(c['count'])
        outfile.write("Case #"+str(cout)+": "+str(c['count'])+"\n")
    print 'done'
    infile.close()
    outfile.close()
    
         

    