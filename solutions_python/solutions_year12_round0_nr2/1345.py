def count(scores, p, numSur):
    count=0
    for s in scores:
        if (p==1 or p==2) and s<p: pass
        elif s>=(3*p-2): count=count+1
        elif s>=(3*p-4) and numSur:
            numSur=numSur-1
            count=count+1
    return count

def process():
    f = open('B-large.in', 'r')
    T=f.readline()
    n=1
    for i in range(int(T)):
        scores=[]
        l=f.readline()
        vals= l.split()
        N=int(vals[0])
        numSur=int(vals[1])
        p=int(vals[2])
        for j in range(N):
            scores.append(int(vals[3+j]))
            
        print "Case #" + str(n)+": "+str(count(scores, p, numSur))
        n=n+1

process()
