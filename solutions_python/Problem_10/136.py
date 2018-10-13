

def pressings(K,L,abc0):
    sum = 0
    abc = sorted(abc0)
    abc.reverse()
    for i in range(0, L):
        sum = sum + abc[i]*(1+i/K)
    return sum

#print pressings(3,6, [1000,300,800,100,7,2])


f = open("A-large.in")
N = int(f.readline())
for i in range(0,N):
    print "Case #%d: "%(i+1),
    [P,K,L] = map(int, f.readline().split())
    abc0 = map(int, f.readline().split())
    print pressings(K,L,abc0)
    
