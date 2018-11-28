#inputdatahere
data="""
"""
sol=[]
data=data.split("\n")
testcases=int(data[0])
for zxc in xrange(testcases):
    print zxc
    w=zxc*3
    x=data[w+2]
    y=data[w+3]
    naomi=[float(i) for i in x.split(" ")]
    ken=[float(i) for i in y.split(" ")]
    naomi=sorted(naomi)
    #print naomi
    ken=sorted(ken)
    #print ken
    ken1=list(ken)
    naomi1=list(naomi)
    played=0
    naomiwin=0
    x=len(naomi)
    while played<x:
        played+=1
        if len(naomi1)>1:
            if max(naomi1)>max(ken1):
                naomiwin+=1
                del naomi1[naomi1.index(max(naomi1))]
                del ken1[ken1.index(min(ken1))]
            else:
                del naomi1[naomi1.index(max(naomi1))]
                del ken1[ken1.index(max(ken1))]
        else:
             if naomi1[0]>ken1[0]:
                naomiwin+=1
    #print naomiwin,played
    played=0
    c=0
    print naomi
    print ken
    naomi2=list(naomi)
    ken2=list(ken)
    for i in xrange(len(ken2)):
        for j in xrange(len(naomi2)):
            if ken2[i]<naomi2[j] and naomi2[j]!=-1 and ken2[i]!=-1:
                c+=1
                naomi2[j]=-1
                ken2[i]=-1
    naomideceit=c
    #print naomideceit,played
    sol.append((naomideceit,naomiwin))
print sol
f=open('problem4.txt','w')
p=1
for i in sol:
    f.write('Case #')
    f.write(str(p))
    f.write(': ')
    f.write(str(i[0]))
    f.write(' ')
    f.write(str(i[1]))
    f.write('\n')
    p+=1
f.close()
