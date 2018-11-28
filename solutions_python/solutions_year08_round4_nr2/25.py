from math import sqrt
from math import pow


def solve2(data):
    print data;
    [N,M,A]=data;
    rez="IMPOSSIBLE";
    for i in range(1,N+1):
        #print "i", i, (A % i == 0),(int(A/i) <= M);
        if (A % i == 0) and (int(A/i) <= M):
            rez="%s %s %s %s %s %s" % (0, 0, i, 0, int(A/i), 0);
            print "rez:", i, rez;
            break;
            
    for i in range(1,M+1):
        #print "i", i;
        if (A % i == 0) and (int(A/i) <= N):
            rez="%s %s %s %s %s %s" % (0, 0, 0, i, 0, int(A/i));
            print "rez:", i, rez;
            break;

    print N,M,A;
    return rez;

def doubleArea(a1,a2,a3):
    return abs(-a2[0]*a1[1]+a3[0]*a1[1]+a1[0]*a2[1]-a3[0]*a2[1]-a1[0]*a3[1]+a2[0]*a3[1]);

def solve(data):
    print data;
    [N,M,A]=data;
    p=[];
    for i in range(N+1):
        for j in range(M+1):
            p.append([i,j]);
            #print [i,j];
    rez="IMPOSSIBLE";
    if (N*M < A):
        return rez;
    for ai in range(len(p)):
        for bi in range(ai, len(p)):
            for ci in range(bi, len(p)):
                a=p[ai];
                b=p[bi];
                c=p[ci];
                if (doubleArea(a,b,c) ==A):
                   rez="%s %s %s %s %s %s" % (a[0], a[1], b[0], b[1], c[0], c[1]);
                   return rez;
    return rez;
            
        

   
def solveAll():
    name="B-small-attempt1";
    
    fi=open("C:/" + name + ".in", "r");
    fo=file("C:/" + name + ".out", "w");

    n=int(fi.readline());
    print "n", n;
    
    for i in range(n):
        #print "i",i;

        
        data=[int(xx) for xx in fi.readline().rstrip().split(" ")];
        
        rez=solve(data);
        rezs=str(rez);

        print "rez", rez;
        print "rezs", rezs;
           
        rezString="Case #%s: %s\n" % ((i+1), rezs);
        print rezString;
        fo.write(rezString);

    fo.close();


solveAll()
#print solve([10, 10, 5])
