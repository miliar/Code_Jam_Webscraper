

def bestSpeed(horses,D):
    minSpeed=10**20
    for h in horses:
        if h[0]<D:
            s=D/((D-h[0])/h[1])
            if s<minSpeed:
                minSpeed=s

    return minSpeed






f=open("prob1large.txt","r")
T=int(f.readline())
ans=[]
for i in xrange(T):
    D,N=[int(x) for x in f.readline().split(' ')]
    horses=[]
    for j in xrange(N):
        h=[float(x) for x in f.readline().split(' ')]
        horses.append(h)

    ans.append(bestSpeed(horses,D))

f.close()

b=open("ans1large.txt","w")
for i in xrange(len(ans)):
    b.write("Case #"+str(i+1)+": %.6f\n"%ans[i])


b.close()
