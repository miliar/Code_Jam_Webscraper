import fileinput,math
outr=open('out.txt','w')
l = [ map(int,line.split()) for line in fileinput.input('C-small-2-attempt0.in') ]
r=l[0][0]
def split(N,K):
    if N==1:
        s1,s2=0,0     #s1 ans s2 are two subsections of original stall problem
    elif N==2:
        s1,s2=K%2,0
    else:
        if K==1:
            s1,s2=int(math.ceil(float(N-1)/2)),int(math.floor(float(N-1)/2))
        else:
            if K%2==0:
                s1,s2=split(math.ceil(float(N-1)/2),K/2)
            else:
                s1,s2=split(math.floor(float(N-1)/2),K/2)
    return [s1,s2]
for i in range(1,r+1):
    N,K=l[i][0],l[i][1]
    s1,s2=split(N,K)
    outr.write('Case #%d: %d %d\n'%(i,s1,s2))
outr.close()

        