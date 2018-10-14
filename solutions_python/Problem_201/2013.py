import sys
def bath(N,k):
    if N==1 and k==1:
        return(0,0)
    elif N%2==0 and k==1:
        return (N/2,N/2-1)
    elif N%2!=0 and k==1:
        return ((N -1)/ 2, ((N-1) / 2) )
    else:
        x=[]
        (y, z) = bath(N,1)
        x.append(y)
        x.append(z)
        for i in range(2,k+1):
            x.sort(reverse=True)
            (y,z)=bath(x[i-2],1)
            x.append(y)
            x.append(z)
        return (y,z)





f1 = open('C-small-1-attempt2.in', 'r')
# f1 = open('test3.txt', 'r')
T=f1.readline().strip()
print T
for t,line in enumerate(f1):
    [N,k] = line.split()
    a=list(bath(int(N), int(k)))
    if a[1]== -1:
        a[1]=0
    sys.stdout = open('bath10.txt', 'a')
    print 'Case #%d: %d %d' % (t + 1, a[0],a[1])
    # print bath(int(N), int(k))