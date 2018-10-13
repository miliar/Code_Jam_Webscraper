f=open("A_large.in",'r')
g=open("A_large.out",'w')
t=int(f.readline())
print t
def pow2(x):
    if x==0: return 1
    return 2*pow2(x-1)
for ind in range(t):
    a = [long(x) for x in f.readline().split()]
    n=a[0];k=a[1];
    
    bool = ((k%pow2(n))==pow2(n)-1)
    s = "OFF"
    if bool: s = "ON"
    print n,k,s
    g.write("Case #"+str(ind+1)+": "+s+"\n")