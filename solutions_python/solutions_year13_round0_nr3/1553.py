

def go():
    f=open('C-large-1.in')
    outf=open('2out.txt','w')
    for x in range(int(f.readline())):
        outf.write('Case #%d: '%(x+1)+str(solve(f))+'\n')
    f.close()

def solve(f):
    r=0
    a,b=[int(x) for x in f.readline().split()]
    l=getlist()
    for x in l:
        if a<=x and x<=b:
            r+=1
    return r


def makelist(a,b): #generated list
    r=0
    #a,b=[int(x) for x in f.readline().split()]
    low=int(a**.5)
    high=int(b**.5)
    for x in range(low,high+1):
        if pal(x) and pal(x**2) and x**2>=a and x**2<=b:
            print x**2
    return r


def pal(n):
    n=list(str(n))
    if n==n[::-1]:
        return 1
    return 0
        

def getlist():
    l='''1
    4
    9
    121
    484
    10201
    12321
    14641
    40804
    44944
    1002001
    1234321
    4008004
    100020001
    102030201
    104060401
    121242121
    123454321
    125686521
    400080004
    404090404
    10000200001
    10221412201
    12102420121
    12345654321
    40000800004
    1000002000001
    1002003002001
    1004006004001
    1020304030201
    1022325232201
    1024348434201
    1210024200121
    1212225222121
    1214428244121
    1232346432321
    1234567654321
    4000008000004
    4004009004004'''.split()
    l=[int(x) for x in l]
    return l
