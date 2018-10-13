def gcd(a,b):
    if a==b: return a
    if a==0: return b
    if b==0: return a
    if a>b: return gcd(a%b,b)
    return gcd(a,b%a)

ifile="B-large.in"
ofile="output.txt"
fi = open(ifile,"r")
fo = open(ofile,"w")
T = int(fi.readline().strip())
for t in range(1,T+1):
    st=fi.readline().strip()
    lis=st.split(' ')
    for i in range(len(lis)):
        lis[i]=long(lis[i])
    g=abs(lis[2]-lis[1])
    for i in range(2,lis[0]):
        g=gcd(g,abs(lis[i+1]-lis[i]))
    ans=g-(lis[1]%g)
    if ans==g: ans=0
    fo.write(format("Case #%d: %ld\n" % (t,ans)))

    
fi.close()
fo.close()