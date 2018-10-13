finp=open('C-small-attempt0.in')
Table=[[0,1,2,3,4,5,6,7],[1,4,3,6,5,0,7,2],[2,7,4,1,6,3,0,5],[3,2,5,4,7,6,1,0],[4,5,6,7,0,1,2,3],[5,0,7,2,1,4,3,6],[6,3,0,5,2,7,4,1],[7,6,1,0,3,2,5,4]]
def Convert(s):
    a=[0]*len(s)
    for i in range(0,len(s)):
        if s[i]=='1':
            a[i]=0
        elif s[i]=='i':
            a[i]=1
        elif s[i]=='j':
            a[i]=2
        else:
            a[i]=3
    return a

Input=finp.read().split()
T=int(Input[0])
fout=open('Outputdijkstras.out','w')
for run in range(1,T+1):
    L=int(''.join(Input[(3*run)-2]))
    X=int(''.join(Input[(3*run)-1]))
    Inp=''.join(Input[3*run])
    C=''
    i=False
    j=False
    k=False
    Findi=True
    Findj=False
    Findk=False
    Inp=Convert(Inp)
    for x in range(X):
        for t in range(0,len(Inp)):
            if C=='':
                C=Inp[t]
            else:
                C=Table[C][Inp[t]]
            if Findi==True and C==1:
                i=True
                C=''
                Findi=False
                Findj=True
            elif Findj==True and C==2:
                j=True
                C=''
                Findk=True
                Findj=False
            elif Findk==True:
                if C==3 and x==X-1 and t==len(Inp)-1:
                    k=True
                else:
                    continue
    Output=i and j and k
    if Output:
        fout.write("Case #%d: YES\n" %run)
    else:
        fout.write("Case #%d: NO\n" %run)
    run+=1
fout.close()
finp.close()
