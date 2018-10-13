f=open("A-large.in")

n=int(f.readline())

for i in range(n):
    ll=[int(x) for x in (f.readline()).split(" ")]
    N=ll[0]
    K=ll[1]
    res="OFF"
    if (K+1)%(2**N)==0: res="ON"
    print "Case #"+str(i+1)+": "+res
