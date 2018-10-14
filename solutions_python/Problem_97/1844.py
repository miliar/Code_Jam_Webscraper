import sys

t = int(sys.stdin.readline())
for times in range(1, t+1):
    recycled_pairs=[]
    a,b = sys.stdin.readline().strip().split()
    a=int(a)
    b=int(b)
    for i in range(a,b+1):
        istr=str(i)
        for j in range(1,len(istr)):
            r=int(istr[len(istr)-j:]+istr[:len(istr)-j])
            if r>=a and r<=b and r>i and [i,r] not in recycled_pairs:
                recycled_pairs.append([i,r])
    print 'Case #'+str(times)+': '+str(len(recycled_pairs))

        
