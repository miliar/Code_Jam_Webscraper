def solve(N,S,p,sums):
    count=0
    for x in range(len(sums)):
        keep=True
        for i in range(11):
            for j in range(11):
                for k in range(11):
                    if i>=p or j>=p or k>=p:
                        if keep and (i+j+k)<=sums[x] and abs(i-j)<=1 and abs(i-k)<=1 and abs(k-j)<=1:
                            count+=1
                            keep=False
                            sums[x]=-1
    for x in range(len(sums)):
        if sums[x]==-1:
            continue
        keep=True
        for i in range(11):
            for j in range(11):
                for k in range(11):
                    if i>=p or j>=p or k>=p:
                        if keep and (i+j+k)<=sums[x] and S>0 and abs(i-j)<=2 and abs(i-k)<=2 and abs(k-j)<=2:
                            count+=1
                            S-=1
                            keep=False
    return count

        
finput='dancingwithgooglers.in'
foutput='dancingwithgooglers.out'

ifile=open(finput,"r")
ofile=open(foutput,"w")

T=int(ifile.readline().strip('\n'))
for i in range(T):
    l=[int(x) for x in ifile.readline().strip('\n').split()]
    N=l[0]
    S=l[1]
    p=l[2]
    sums=list()
    for e in range(N):
        sums.append(l[e+3])
    r=solve(N,S,p,sums)
    
    print('Case #'+str(i+1)+':',r,file=ofile)
    print('Case #'+str(i+1)+':',r)

ifile.close()
ofile.close()
