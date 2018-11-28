fl=file("A-small-attempt0.in","r")
fo=file("output1.txt","w")
t=int(fl.readline())
for i in xrange(t):
    ans1=int(fl.readline())
    nu1=[]*5
    nu2=[]*5
    for j in xrange(4):
        if j+1==ans1:
            nu1=map(int,fl.readline().split())
        else:
            fl.readline()
    ans2=int(fl.readline())
    row2=[]*5
    for j in xrange(4):
        if j+1==ans2:
            nu2=map(int,fl.readline().split())
        else:
            fl.readline()
    count=0
    for j in nu1:
        if j in nu2:
            count+=1
            n=j
    if(count==1):
        fo.write("Case #%d: %d\n"%(i+1,n))
    elif count==0:
        fo.write("Case #%d: Volunteer Cheated!\n"%(i+1))
    else:
        fo.write("Case #%d: Bad Magician!\n"%(i+1))
fl.close()
fo.close()
