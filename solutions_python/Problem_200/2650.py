File=open("B-large.txt",'w')

T=int(raw_input())
for t in range(T):
    N=[int(n) for n in raw_input()]
    i=len(N)-1
    j=len(N)
    while i>0:
        if N[i]<N[i-1]: 
            N[i-1]=N[i-1]-1
            for k in range(i,j):
                N[k]=9
            j=i
        i=i-1
    N=[str(n) for n in N]
    y=int(''.join(N))
    print >> File, "Case #%d: %d" %(t+1,y)

File.close()
