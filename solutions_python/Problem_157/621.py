lines=[]
file1=open('C-small-attempt0.in')
for line in file1:
    lines.append(line)
file1.close

#0,1,2,3 = 1,i,j,k
#4,5,6,7 = -1,-i,-j,-k
Table=[[0,1,2,3,4,5,6,7],[1,4,3,6,5,0,7,2],[2,7,4,1,6,3,0,5],[3,2,5,4,7,6,1,0],[4,5,6,7,0,1,2,3],[5,0,7,2,1,4,3,6],[6,3,0,5,2,7,4,1],[7,6,1,0,3,2,5,4]]
def Mult(i,j):
    return Table[i][j]
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

def Match(S):
    C=S[0]
    idx=1
    i=True
    j=True
    k=True
    while C!=1 and idx<len(S):
        C=Mult(C,S[idx])
        idx+=1
    if idx==len(S):
        i=False
        return False
    C=S[idx]
    idx+=1
    while C!=2 and idx<len(S):
        C=Mult(C,S[idx])
        idx+=1
    if idx==len(S):
        j=False
        return False
    C=S[idx]
    idx+=1
    while idx<len(S):
        C=Mult(C,S[idx])
        idx+=1
    if C!=3:
        k=False
        return False
    return True
    
T=int(lines[0])
ctr=1
f=open('Output.out','w')
while ctr<=T:
    L,X=[int(x) for x in lines[(2*ctr) - 1].split()]#raw_input().split()]
    Inp=lines[2*ctr].split()#raw_input()
    #Inp=Inp[0:len(Inp)-1]
    Str=Inp*X
    Final=''.join(Str)
    S=Convert(Final)
    Output=Match(S)
    if Output:
        f.write("Case #%d: YES" %ctr)#print "Case #%d: YES" %(ctr)
    else:
        f.write("Case #%d: NO" %ctr)#print "Case #%d: NO" %ctr
    ctr+=1
    if ctr<=T:
        f.write("\n")
f.close()
