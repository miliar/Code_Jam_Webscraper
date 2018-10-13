f=open('A-large.in')
out=open('output.txt','w')
T=int(f.readline())
for i in range(T):
    out.write('Case #'+str(i+1)+': ')
    pl=1
    n=0
    temp=f.readline().split()
    #pancake=temp[0]
    S=len(temp[0])
    K=int(temp[1])
    pancake = [0 for j in range(S)]
    for j in range(S):
        if temp[0][j]=='-':
            pancake[j]=1 #'-'
    if sum(pancake)==0:
        out.write('0\n')
        continue
    for j in range(S):
        if pancake[j]==1:
            if j>=(S-K+1):
                pl=0
                out.write('IMPOSSIBLE\n')
                break
            else:
                n=n+1
                for k in range(K):
                    pancake[j+k]=1-pancake[j+k]
            #for t in range(S):
            #    out.write(str(pancake[t]))
            #out.write('\n')
    if pl==1:
        out.write(str(n)+'\n')
f.close()
out.close()
