import fileinput,math
def corr(N,K):
    if N==1:
        y,z=0,0
    elif N==2:
        y,z=K%2,0
    else:
        if K==1:
            y,z=int(math.ceil(float(N-1)/2)),int(math.floor(float(N-1)/2))
        else:
            if K%2==0:
                y,z=corr(math.ceil(float(N-1)/2),K/2)
            else:
                y,z=corr(math.floor(float(N-1)/2),K/2)
    return [y,z]
l = [ map(int,line.split()) for line in fileinput.input('C-small-2-attempt0.in') ]
outr=open('out.txt','w')
r=l[0][0]
for i in range(1,r+1):
    N,K=l[i][0],l[i][1]
    y,z=corr(N,K)
    outr.write('Case #%d: %d %d\n'%(i,y,z))
outr.close()